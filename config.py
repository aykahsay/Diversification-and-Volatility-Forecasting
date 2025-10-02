import os
from pydantic_settings import BaseSettings  # <-- changed import

def return_full_path(filename: str = ".env") -> str:
    """Return the full absolute path to the .env file"""
    absolute_path = os.path.abspath(__file__)
    directory_name = os.path.dirname(absolute_path)
    return os.path.join(directory_name, filename)

class Settings(BaseSettings):
    alpha_api_key: str
    db_name: str
    model_directory: str

    class Config:
        env_file = return_full_path(".env")

settings = Settings()