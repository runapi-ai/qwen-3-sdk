import pytest

from runapi.core import config
from runapi.core.errors import AuthenticationError, ValidationError
from runapi.qwen_3 import Qwen3Client
from runapi.qwen_3.resources.edit_image import EditImage
from runapi.qwen_3.resources.text_to_image import TextToImage
from runapi.qwen_3.types import (
    CompletedTextToImageResponse,
    EditImageResponse,
    TextToImageResponse,
)


class FakeHttp:
    def __init__(self, *responses):
        self._responses = list(responses)
        self.calls = []

    def request(self, method, path, body=None, options=None):
        self.calls.append((method, path, body))
        if self._responses:
            return self._responses.pop(0)
        return {"id": "task_1", "status": "pending"}


@pytest.fixture(autouse=True)
def reset_config(monkeypatch):
    monkeypatch.delenv("RUNAPI_API_KEY", raising=False)
    monkeypatch.setattr(config, "api_key", None)
    yield


# --- auth -----------------------------------------------------------------


def test_accepts_api_key_parameter():
    assert isinstance(Qwen3Client(api_key="k", http_client=FakeHttp()), Qwen3Client)


def test_falls_back_to_global(monkeypatch):
    monkeypatch.setattr(config, "api_key", "global-key")
    assert isinstance(Qwen3Client(http_client=FakeHttp()), Qwen3Client)


def test_falls_back_to_env(monkeypatch):
    monkeypatch.setenv("RUNAPI_API_KEY", "env-key")
    assert isinstance(Qwen3Client(http_client=FakeHttp()), Qwen3Client)


def test_raises_without_api_key():
    with pytest.raises(AuthenticationError, match="API key is required"):
        Qwen3Client()


# --- injection / accessors ------------------------------------------------


def test_uses_injected_http_client():
    fake = FakeHttp()
    client = Qwen3Client(api_key="k", http_client=fake)
    assert client.text_to_image._http is fake
    assert client.edit_image._http is fake


def test_exposes_resource_accessors():
    client = Qwen3Client(api_key="k", http_client=FakeHttp())
    assert isinstance(client.text_to_image, TextToImage)
    assert isinstance(client.edit_image, EditImage)


# --- request shapes -------------------------------------------------------


def test_create_posts_compacted_body():
    fake = FakeHttp({"id": "t1", "status": "pending"})
    client = Qwen3Client(api_key="k", http_client=fake)
    result = client.text_to_image.create(
        model="qwen-3-text-to-image", prompt="hello world", aspect_ratio="1:1", output_format=None
    )
    assert fake.calls == [
        ("post", "/api/v1/qwen_3/text_to_image", {"model": "qwen-3-text-to-image", "prompt": "hello world", "aspect_ratio": "1:1"})]
    assert isinstance(result, TextToImageResponse)


def test_get_fetches_by_id():
    fake = FakeHttp({"id": "t1", "status": "processing"})
    client = Qwen3Client(api_key="k", http_client=fake)
    client.text_to_image.get("t1")
    assert fake.calls == [("get", "/api/v1/qwen_3/text_to_image/t1", None)]


def test_edit_image_create_posts_compacted_body():
    fake = FakeHttp({"id": "e1", "status": "pending"})
    client = Qwen3Client(api_key="k", http_client=fake)
    result = client.edit_image.create(
        model="qwen-3-edit-image",
        prompt="make it pop",
        source_image_urls=["https://x/in.jpg", "https://x/reference.jpg"],
    )
    assert fake.calls == [
        (
            "post",
            "/api/v1/qwen_3/edit_image",
            {
                "model": "qwen-3-edit-image",
                "prompt": "make it pop",
                "source_image_urls": ["https://x/in.jpg", "https://x/reference.jpg"]},
        )]
    assert isinstance(result, EditImageResponse)


def test_run_narrows_completed_type():
    fake = FakeHttp(
        {"id": "t1", "status": "pending"},
        {"id": "t1", "status": "completed", "usage": {"cost": 0.05}, "images": [{"url": "https://x/y.png"}]},
    )
    client = Qwen3Client(api_key="k", http_client=fake)
    result = client.text_to_image.run(model="qwen-3-text-to-image", prompt="a serene lake")
    assert isinstance(result, CompletedTextToImageResponse)
    assert result.images[0].url == "https://x/y.png"


# --- validation -----------------------------------------------------------


def test_rejects_unknown_model():
    client = Qwen3Client(api_key="k", http_client=FakeHttp())
    with pytest.raises(ValidationError, match="model must be one of"):
        client.text_to_image.create(model="nope", prompt="hi there")


def test_requires_prompt():
    client = Qwen3Client(api_key="k", http_client=FakeHttp())
    with pytest.raises(ValidationError, match="prompt is required"):
        client.text_to_image.create(model="qwen-3-text-to-image")


def test_text_to_image_rejects_bad_aspect_ratio():
    client = Qwen3Client(api_key="k", http_client=FakeHttp())
    with pytest.raises(ValidationError, match="aspect_ratio"):
        client.text_to_image.create(model="qwen-3-text-to-image", prompt="hi there", aspect_ratio="5:1")


def test_edit_image_requires_source_image_urls():
    client = Qwen3Client(api_key="k", http_client=FakeHttp())
    with pytest.raises(ValidationError, match="source_image_urls is required"):
        client.edit_image.create(model="qwen-3-edit-image", prompt="make it pop")


def test_rejects_bad_output_format():
    client = Qwen3Client(api_key="k", http_client=FakeHttp())
    with pytest.raises(ValidationError, match="output_format"):
        client.edit_image.create(
            model="qwen-3-edit-image",
            prompt="edit this",
            source_image_urls=["https://x/in.jpg"],
            output_format="webp",
        )
