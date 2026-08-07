package ai.runapi.qwen3.types;

import com.fasterxml.jackson.annotation.JsonCreator;

/** Model slug for text to image operations. */
public final class TextToImageModel extends Qwen3Value {
  /** qwen-3-pro-text-to-image model slug. */
  public static final TextToImageModel QWEN_3_PRO_TEXT_TO_IMAGE = new TextToImageModel("qwen-3-pro-text-to-image");
  /** qwen-3-text-to-image model slug. */
  public static final TextToImageModel QWEN_3_TEXT_TO_IMAGE = new TextToImageModel("qwen-3-text-to-image");

  /** Creates a model value from a literal model slug. */
  @JsonCreator
  public TextToImageModel(String value) {
    super(value);
  }
}
