import os

class DefaultConfig:
    PORT = int(os.environ.get("PORT", 8000))

    # Azure Bot / App Registration
    MicrosoftAppId = os.environ.get("MicrosoftAppId", "")
    MicrosoftAppPassword = os.environ.get("MicrosoftAppPassword", "")
    MicrosoftAppType = os.environ.get("MicrosoftAppType", "SingleTenant")
    MicrosoftAppTenantId = os.environ.get("MicrosoftAppTenantId", "")

    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_DEPLOYMENT = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "")
    AZURE_OPENAI_API_VERSION = os.environ.get(
        "AZURE_OPENAI_API_VERSION", "2024-10-21"
    )