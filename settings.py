from pydantic import ValidationError, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    # @validator("environment") # obsolete
    @field_validator("environment", mode="before")
    @classmethod
    def validate_environment(cls, value):
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        if value not in ["dev", "test", "prod"]:
            raise ValidationError("Environment must be 'dev' or 'test' or 'prod'")
        return value
