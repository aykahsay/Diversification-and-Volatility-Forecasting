import os
from pydantic_settings import BaseSettings

# Function to get the full path of the .env file
def return_full_path(filename: str = ".env") -> str:
    return os.path.join(os.getcwd(), filename)

class Settings(BaseSettings):
    alpha_api_key: str
    db_name: str
    model_directory: str

    class Config:
        env_file = return_full_path(".env")  # Use the full path for the .env file

# Initialize Settings class
settings = Settings()

# Debugging: Print the loaded settings
print("Alpha API Key:", settings.alpha_api_key)
print("Database Name:", settings.db_name)
print("Model Directory:", settings.model_directory)
