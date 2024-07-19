from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    HOST: str = "localhost"
    PORT: int = 27017
    USERNAME: str = ""
    PASSWORD: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        secrets_dir="/run/secrets",
        extra="ignore",
        env_prefix="mongodb_",
    )
