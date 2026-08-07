package ai.runapi.qwen3.types;

import com.fasterxml.jackson.annotation.JsonCreator;

/** Model slug for edit image operations. */
public final class EditImageModel extends Qwen3Value {
  /** qwen-3-edit-image model slug. */
  public static final EditImageModel QWEN_3_EDIT_IMAGE = new EditImageModel("qwen-3-edit-image");
  /** qwen-3-pro-edit-image model slug. */
  public static final EditImageModel QWEN_3_PRO_EDIT_IMAGE = new EditImageModel("qwen-3-pro-edit-image");

  /** Creates a model value from a literal model slug. */
  @JsonCreator
  public EditImageModel(String value) {
    super(value);
  }
}
