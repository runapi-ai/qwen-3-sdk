CONTRACT = {
    "edit-image": {
        "models": ["qwen-3-edit-image", "qwen-3-pro-edit-image"],
        "fields_by_model": {
            "qwen-3-edit-image": {
                "aspect_ratio": {
                    "enum": ["1:1", "3:2", "2:3", "4:3", "3:4", "16:9", "9:16", "21:9"]
                },
                "model": {
                    "required": True
                },
                "negative_prompt": {
                    "min": 0,
                    "max": 5000,
                    "length": True
                },
                "output_format": {
                    "enum": ["png", "jpeg"]
                },
                "output_resolution": {
                    "enum": ["1k", "2k"]
                },
                "prompt": {
                    "required": True,
                    "min": 1,
                    "max": 800,
                    "length": True
                },
                "seed": {
                    "min": 0,
                    "max": 2147483647,
                    "type": "integer"
                },
                "source_image_urls": {
                    "required": True,
                    "min_items": 1,
                    "max_items": 3
                }
            },
            "qwen-3-pro-edit-image": {
                "aspect_ratio": {
                    "enum": ["1:1", "3:2", "2:3", "4:3", "3:4", "16:9", "9:16", "21:9"]
                },
                "model": {
                    "required": True
                },
                "negative_prompt": {
                    "min": 0,
                    "max": 5000,
                    "length": True
                },
                "output_format": {
                    "enum": ["png", "jpeg"]
                },
                "output_resolution": {
                    "enum": ["1k", "2k"]
                },
                "prompt": {
                    "required": True,
                    "min": 1,
                    "max": 800,
                    "length": True
                },
                "seed": {
                    "min": 0,
                    "max": 2147483647,
                    "type": "integer"
                },
                "source_image_urls": {
                    "required": True,
                    "min_items": 1,
                    "max_items": 3
                }
            }
        }
    },
    "text-to-image": {
        "models": ["qwen-3-pro-text-to-image", "qwen-3-text-to-image"],
        "fields_by_model": {
            "qwen-3-pro-text-to-image": {
                "aspect_ratio": {
                    "enum": ["1:1", "3:2", "2:3", "4:3", "3:4", "16:9", "9:16", "21:9"]
                },
                "model": {
                    "required": True
                },
                "negative_prompt": {
                    "min": 0,
                    "max": 5000,
                    "length": True
                },
                "output_format": {
                    "enum": ["png", "jpeg"]
                },
                "output_resolution": {
                    "enum": ["1k", "2k"]
                },
                "prompt": {
                    "required": True,
                    "min": 1,
                    "max": 800,
                    "length": True
                },
                "seed": {
                    "min": 0,
                    "max": 2147483647,
                    "type": "integer"
                }
            },
            "qwen-3-text-to-image": {
                "aspect_ratio": {
                    "enum": ["1:1", "3:2", "2:3", "4:3", "3:4", "16:9", "9:16", "21:9"]
                },
                "model": {
                    "required": True
                },
                "negative_prompt": {
                    "min": 0,
                    "max": 5000,
                    "length": True
                },
                "output_format": {
                    "enum": ["png", "jpeg"]
                },
                "output_resolution": {
                    "enum": ["1k", "2k"]
                },
                "prompt": {
                    "required": True,
                    "min": 1,
                    "max": 800,
                    "length": True
                },
                "seed": {
                    "min": 0,
                    "max": 2147483647,
                    "type": "integer"
                }
            }
        }
    }
}
