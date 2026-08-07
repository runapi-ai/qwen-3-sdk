package ai.runapi.qwen3.resources;

import ai.runapi.core.ClientOptions;
import ai.runapi.core.RequestOptions;
import ai.runapi.core.http.HttpTransport;
import ai.runapi.core.polling.TaskCreateResponse;
import ai.runapi.qwen3.types.CompletedEditImageResponse;
import ai.runapi.qwen3.types.EditImageParams;
import ai.runapi.qwen3.types.EditImageResponse;

/** Image To Image operations. */
public final class EditImageResource extends Qwen3Resource {
  /** API endpoint path for image to image operations. */
  public static final String ENDPOINT = "/api/v1/qwen_3/edit_image";

  /** Creates a resource bound to the supplied transport and client options. */
  public EditImageResource(HttpTransport transport, ClientOptions options) {
    super(transport, options, ENDPOINT);
  }

  /** Creates a image to image task. */
  public TaskCreateResponse create(EditImageParams params) {
    return create(params, RequestOptions.none());
  }

  /** Creates a image to image task with per-request options. */
  public TaskCreateResponse create(EditImageParams params, RequestOptions options) {
    return createTask(params.action(), params.toMap(), options);
  }

  /** Retrieves a image to image task by ID. */
  public EditImageResponse get(String id) {
    return get(id, RequestOptions.none());
  }

  /** Retrieves a image to image task by ID with per-request options. */
  public EditImageResponse get(String id, RequestOptions options) {
    return getTask(id, options, EditImageResponse.class);
  }

  /** Creates a image to image task and polls until it completes. */
  public CompletedEditImageResponse run(EditImageParams params) {
    return run(params, RequestOptions.none());
  }

  /** Creates a image to image task with per-request options and polls until it completes. */
  public CompletedEditImageResponse run(EditImageParams params, RequestOptions options) {
    return runTask(params.action(), params.toMap(), options, EditImageResponse.class, CompletedEditImageResponse.class);
  }
}
