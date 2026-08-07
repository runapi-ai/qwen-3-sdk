import type { AsyncTaskStatus, TaskBillingResponse, TaskResponse } from '@runapi.ai/core';

/** All Qwen 3 model variants, each dedicated to a single operation type. */
export type Qwen3Model =
  | 'qwen-3-edit-image'
  | 'qwen-3-pro-edit-image'
  | 'qwen-3-pro-text-to-image'
  | 'qwen-3-text-to-image';

/** Aspect ratio options for edit-image. Wider set than text-to-image, includes ultra-wide 21:9. */
export type EditImageAspectRatio = '1:1' | '2:3' | '3:2' | '3:4' | '4:3' | '9:16' | '16:9' | '21:9';
/** Aspect ratio options for text-to-image generation. Default: 16:9. */
export type TextToImageAspectRatio = EditImageAspectRatio;
/** Output image encoding format. */
export type OutputFormat = 'jpeg' | 'png';
/** Output image resolution. */
export type OutputResolution = '1k' | '2k';

/** Parameters for text-to-image generation. Prompt up to 800 characters. */
export interface TextToImageParams {
  model: 'qwen-3-text-to-image' | 'qwen-3-pro-text-to-image';
  /** Image description (up to 800 chars). */
  prompt: string;
  output_resolution?: OutputResolution;
  aspect_ratio?: TextToImageAspectRatio;
  /** Integer seed for reproducible results. */
  seed?: number;
  output_format?: OutputFormat;
  /** Expand the prompt before generation. */
  enable_prompt_expansion?: boolean;
  /** Toggle content safety filtering. */
  enable_safety_checker?: boolean;
  /** Content to avoid in the generated image (up to 5000 chars). */
  negative_prompt?: string;
  /** Webhook URL for async completion notifications. */
  callback_url?: string;
}

/** Parameters for edit-image. Applies prompt-described changes to a source image. */
export interface EditImageParams {
  model: 'qwen-3-edit-image' | 'qwen-3-pro-edit-image';
  /** Edit instruction (1-800 chars). */
  prompt: string;
  /** One to three public source image URLs. */
  source_image_urls: string[];
  output_resolution?: OutputResolution;
  aspect_ratio?: EditImageAspectRatio;
  output_format?: OutputFormat;
  /** Expand the prompt before generation. */
  enable_prompt_expansion?: boolean;
  /** Integer seed for reproducible results. */
  seed?: number;
  /** Toggle content safety filtering. */
  enable_safety_checker?: boolean;
  /** Content to avoid in the generated image (up to 5000 chars). */
  negative_prompt?: string;
  /** Webhook URL for async completion notifications. */
  callback_url?: string;
}

export interface TaskCreateResponse extends TaskBillingResponse {
  id: string;
}

/** A single generated image result. */
export interface Image {
  /** CDN-delivered image URL. */
  url: string;
}

/** Shared task result for all Qwen 3 image operations. */
export interface ImageTaskResponse extends TaskResponse {
  id: string;
  status: AsyncTaskStatus;
  /** Output images, populated once the task completes successfully. */
  images?: Image[];
  /** Error message when the task has failed. */
  error?: string;
  [key: string]: unknown;
}

export type TextToImageResponse = ImageTaskResponse;
export type EditImageResponse = ImageTaskResponse;

/**
 * Resolved responses returned by the `run()` methods after polling sees
 * `status: 'completed'`. Narrows the base response so `images` is
 * guaranteed non-optional in user code.
 */
export type CompletedTextToImageResponse = TextToImageResponse & {
  status: 'completed';
  images: Image[];
};

export type CompletedEditImageResponse = EditImageResponse & {
  status: 'completed';
  images: Image[];
};
