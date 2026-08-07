package ai.runapi.qwen3.types;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/** Parameters for image to image operations. */
public final class EditImageParams {
  private final String model;
  private final String prompt;
  private final List<String> sourceImageUrls;
  private final String outputResolution;
  private final String aspectRatio;
  private final String outputFormat;
  private final Boolean enablePromptExpansion;
  private final Boolean enableSafetyChecker;
  private final String negativePrompt;
  private final Integer seed;
  private final String callbackUrl;

  private EditImageParams(Builder builder) {
    this.model = Qwen3ParamUtils.requireNonBlankTrim(builder.model, "model");
    this.prompt = Qwen3ParamUtils.requireNonBlank(builder.prompt, "prompt");
    this.sourceImageUrls = Qwen3ParamUtils.requiredStrings(builder.sourceImageUrls, "sourceImageUrls");
    this.outputResolution = builder.outputResolution;
    this.aspectRatio = builder.aspectRatio;
    this.outputFormat = builder.outputFormat;
    this.enablePromptExpansion = builder.enablePromptExpansion;
    this.enableSafetyChecker = builder.enableSafetyChecker;
    this.negativePrompt = builder.negativePrompt;
    this.seed = builder.seed;
    this.callbackUrl = builder.callbackUrl;
  }

  /** Creates a new EditImageParams builder. */
  public static Builder builder() {
    return new Builder();
  }

  /** Returns the RunAPI action key for this request. */
  public String action() {
    return "qwen-3/edit-image";
  }

  /** Converts these parameters to the JSON request body shape. */
  public Map<String, Object> toMap() {
    Map<String, Object> raw = new LinkedHashMap<String, Object>();
    raw.put("model", Qwen3ParamUtils.wireValue(model));
    raw.put("prompt", Qwen3ParamUtils.wireValue(prompt));
    raw.put("source_image_urls", Qwen3ParamUtils.wireValue(sourceImageUrls));
    raw.put("output_resolution", Qwen3ParamUtils.wireValue(outputResolution));
    raw.put("aspect_ratio", Qwen3ParamUtils.wireValue(aspectRatio));
    raw.put("output_format", Qwen3ParamUtils.wireValue(outputFormat));
    raw.put("enable_prompt_expansion", Qwen3ParamUtils.wireValue(enablePromptExpansion));
    raw.put("enable_safety_checker", Qwen3ParamUtils.wireValue(enableSafetyChecker));
    raw.put("negative_prompt", Qwen3ParamUtils.wireValue(negativePrompt));
    raw.put("seed", Qwen3ParamUtils.wireValue(seed));
    raw.put("callback_url", Qwen3ParamUtils.wireValue(callbackUrl));
    return Qwen3ParamUtils.compact(raw);
  }



  /** Builder for {@link EditImageParams}. */
  public static final class Builder {
    private String model;
    private String prompt;
    private List<String> sourceImageUrls;
    private String outputResolution;
    private String aspectRatio;
    private String outputFormat;
    private Boolean enablePromptExpansion;
    private Boolean enableSafetyChecker;
    private String negativePrompt;
    private Integer seed;
    private String callbackUrl;

    private Builder() {}

    /** Sets the model slug using a typed model value. */
    public Builder model(EditImageModel value) {
      this.model = java.util.Objects.requireNonNull(value, "model").value();
      return this;
    }

    /** Sets the model slug using a string value. */
    public Builder model(String value) {
      this.model = Qwen3ParamUtils.requireNonBlankTrim(value, "model");
      return this;
    }


    /** Sets the text prompt. */
    public Builder prompt(String value) {
      this.prompt = Qwen3ParamUtils.requireNonBlank(value, "prompt");
      return this;
    }

    /** Sets the source image URLs. */
    public Builder sourceImageUrls(List<String> value) {
      this.sourceImageUrls = value;
      return this;
    }

    /** Sets the output resolution. */
    public Builder outputResolution(String value) {
      this.outputResolution = Qwen3ParamUtils.requireNonBlank(value, "outputResolution");
      return this;
    }

    /** Sets the output aspect ratio. */
    public Builder aspectRatio(String value) {
      this.aspectRatio = Qwen3ParamUtils.requireNonBlank(value, "aspectRatio");
      return this;
    }

    /** Sets the output format. */
    public Builder outputFormat(String value) {
      this.outputFormat = Qwen3ParamUtils.requireNonBlank(value, "outputFormat");
      return this;
    }

    /** Sets the prompt expansion toggle. */
    public Builder enablePromptExpansion(boolean value) {
      this.enablePromptExpansion = value;
      return this;
    }

    /** Sets the content safety checker toggle. */
    public Builder enableSafetyChecker(boolean value) {
      this.enableSafetyChecker = value;
      return this;
    }

    /** Sets the negative prompt describing what to avoid. */
    public Builder negativePrompt(String value) {
      this.negativePrompt = Qwen3ParamUtils.requireNonBlank(value, "negativePrompt");
      return this;
    }

    /** Sets the random seed. */
    public Builder seed(int value) {
      this.seed = value;
      return this;
    }

    /** Sets the webhook URL for task completion notifications. */
    public Builder callbackUrl(String value) {
      this.callbackUrl = Qwen3ParamUtils.requireNonBlank(value, "callbackUrl");
      return this;
    }

    /** Builds immutable image to image parameters. */
    public EditImageParams build() {
      return new EditImageParams(this);
    }
  }
}
