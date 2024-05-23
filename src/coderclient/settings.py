import pydantic
import pydantic_settings

class CoderClientSettings(pydantic_settings.BaseSettings):
    llama_url: str = "http://localhost:8080"

