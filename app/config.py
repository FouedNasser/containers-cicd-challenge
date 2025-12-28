from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # These will be overwritten by environment variables if they exist
    database_url: str = "postgresql://postgres:postgres@db:5432/fastapi_db"
    secret_key: str = "placeholder_secret_key" # This must be changed in production
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
