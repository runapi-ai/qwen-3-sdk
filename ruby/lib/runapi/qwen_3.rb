# frozen_string_literal: true

require "runapi/core"
require_relative "qwen_3/types"
require_relative "qwen_3/contract_gen"
require_relative "qwen_3/resources/text_to_image"
require_relative "qwen_3/resources/edit_image"
require_relative "qwen_3/client"

module RunApi
  module Qwen3
    AuthenticationError = RunApi::Core::AuthenticationError
    RateLimitError = RunApi::Core::RateLimitError
    InsufficientCreditsError = RunApi::Core::InsufficientCreditsError
    NotFoundError = RunApi::Core::NotFoundError
    ValidationError = RunApi::Core::ValidationError
    TaskFailedError = RunApi::Core::TaskFailedError
    TaskTimeoutError = RunApi::Core::TaskTimeoutError
  end
end
