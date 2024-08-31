from typing import Literal

from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: Literal['dev', 'prod'] = 'dev'

    BOT_TOKEN: SecretStr
    
    DATABASE_URL: str
    PGADMIN_USER: SecretStr
    PGADMIN_PASSWORD: SecretStr

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
