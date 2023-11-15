from pydantic import BaseModel
import os
from dotenv import load_dotenv, find_dotenv
import openai

load_dotenv(find_dotenv())


class Settings(BaseModel):
    app_environment: str = "dev"
    ai_base_url: str = os.environ.get("AI_BASE_URL", "")
    qdrant_url: str = os.environ.get("QDRANT", "")
    sentry_dns: str = os.environ.get("SENTRY_DNS", "")
    current_folder: str = os.getcwd()
    project_folder: str = "/backend"


settings = Settings()


openai.api_base = settings.ai_base_url
