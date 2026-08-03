from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str = "DocGen AI"

    API_VERSION: str = "v1"

    GOOGLE_API_KEY: str = ""

    GITHUB_TOKEN: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()