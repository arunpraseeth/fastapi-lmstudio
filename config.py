#Constants, settings, URLs (keeps them in one place)

"""Configuration settings for the application."""

# LM Studio settings
LM_STUDIO_BASE_URL = "http://127.0.0.1:1234"
LM_STUDIO_MODELS_URL = f"{LM_STUDIO_BASE_URL}/v1/models"
LM_STUDIO_CHAT_URL = f"{LM_STUDIO_BASE_URL}/v1/chat/completions"

# Default model parameters
DEFAULT_MODEL = "llama-3.2-1b-instruct"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = -1
DEFAULT_STREAM = False

# HTTP settings
REQUEST_TIMEOUT = 30.0
