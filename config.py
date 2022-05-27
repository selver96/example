
from enum import Enum
from typing import Dict, Type

from pydantic import BaseModel, BaseSettings, Field

class EnvState(Enum):
    DEV = "dev"
    PROD = "prod"


class InternalConfig(BaseModel):
    """Configuration variables that are not required to be read from environment."""

    PROJECT_NAME: str = "EMPLOYEE-SERVICE"
    DB_NAME: str = "category_service_db"


class EnvConfig(BaseSettings):
    ENV_STATE: EnvState = EnvState.DEV


class Config(BaseSettings):

    internal: InternalConfig = InternalConfig()
    env_state: EnvState

    # Global variables
    PORT: int = Field(env="PORT")

    # Environment specific variables
    HOST: str
    TIMEZONE: str = "Turkey"

    @property
    def DEBUG(self) -> bool:
        return self.env_state is EnvState.DEV

    class Config:
        """Loads the dotenv file."""
        env_file: str = ".env"


class DevConfig(Config):
    """Development configurations."""

    class Config:
        env_prefix: str = "DEV_"


class ProdConfig(Config):
    """Production configurations."""

    class Config:
        env_prefix: str = "PROD_"


def create_config(state: EnvState) -> Config:
    config_map: Dict[EnvState, Type[Config]] = {
        EnvState.DEV: DevConfig,
        EnvState.PROD: ProdConfig,
    }
    return config_map[state](env_state=state)


config = create_config(EnvConfig().ENV_STATE)