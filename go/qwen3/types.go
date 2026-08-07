package qwen3

import "github.com/runapi-ai/core-sdk/go/core"

// TaskStatus represents the lifecycle state of an async task.
type TaskStatus string

// TextToImageParams configures a text-to-image generation request.
type TextToImageParams struct {
	Model                 string `json:"model" help:"required; RunAPI model identifier"`
	Prompt                string `json:"prompt" help:"required; image generation prompt; up to 800 characters"`
	OutputResolution      string `json:"output_resolution,omitempty" help:"optional; output image resolution; Default: 1k"`
	AspectRatio           string `json:"aspect_ratio,omitempty" help:"optional; output aspect ratio; Default: 16:9"`
	OutputFormat          string `json:"output_format,omitempty" help:"optional; output image format; Default: png"`
	EnablePromptExpansion *bool  `json:"enable_prompt_expansion,omitempty" help:"optional; expand the prompt before generation; Default: true"`
	EnableSafetyChecker   *bool  `json:"enable_safety_checker,omitempty" help:"optional; check generated content for safety; Default: false"`
	NegativePrompt        string `json:"negative_prompt,omitempty" help:"optional; content to avoid; up to 5000 characters"`
	Seed                  *int   `json:"seed,omitempty" help:"optional; integer seed from 0 to 2147483647; Default: 1"`
	CallbackURL           string `json:"callback_url,omitempty" help:"optional; webhook URL for asynchronous task updates"`
}

// EditImageParams configures an image editing request that applies prompt-described changes
// to a source image.
type EditImageParams struct {
	Model                 string   `json:"model" help:"required; RunAPI model identifier"`
	Prompt                string   `json:"prompt" help:"required; image editing prompt; up to 800 characters"`
	SourceImageURLs       []string `json:"source_image_urls" help:"required; one to three public source image URLs"`
	OutputResolution      string   `json:"output_resolution,omitempty" help:"optional; output image resolution; Default: 1k"`
	AspectRatio           string   `json:"aspect_ratio,omitempty" help:"optional; output aspect ratio; Default: 16:9"`
	OutputFormat          string   `json:"output_format,omitempty" help:"optional; output image format; Default: png"`
	EnablePromptExpansion *bool    `json:"enable_prompt_expansion,omitempty" help:"optional; expand the prompt before generation; Default: true"`
	EnableSafetyChecker   *bool    `json:"enable_safety_checker,omitempty" help:"optional; check generated content for safety; Default: false"`
	NegativePrompt        string   `json:"negative_prompt,omitempty" help:"optional; content to avoid; up to 5000 characters"`
	Seed                  *int     `json:"seed,omitempty" help:"optional; integer seed from 0 to 2147483647; Default: 1"`
	CallbackURL           string   `json:"callback_url,omitempty" help:"optional; webhook URL for asynchronous task updates"`
}

// AsyncTaskResponse implements core.TaskResponse for async task polling.
type AsyncTaskResponse struct {
	core.TaskBillingFacts
	ID     string     `json:"id"`
	Status TaskStatus `json:"status"`
	Error  string     `json:"error,omitempty"`
}

func (r AsyncTaskResponse) GetID() string     { return r.ID }
func (r AsyncTaskResponse) GetStatus() string { return string(r.Status) }
func (r AsyncTaskResponse) GetError() string  { return r.Error }

// Image holds a CDN URL for a generated image.
type Image struct {
	URL string `json:"url"`
}

// ImageTaskResponse is the base response for all Qwen3 image operations.
type ImageTaskResponse struct {
	AsyncTaskResponse
	Images []Image `json:"images,omitempty"`
}

// TextToImageResponse is an alias for ImageTaskResponse.
type TextToImageResponse = ImageTaskResponse

// EditImageResponse is an alias for ImageTaskResponse.
type EditImageResponse = ImageTaskResponse
