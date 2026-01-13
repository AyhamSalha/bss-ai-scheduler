"""Configuration settings for the application."""
import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # Application
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    
    # Database
    database_path: str = "./chat.db"
    
    # LLM Settings
    llm_model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    llm_max_tokens: int = 80
    llm_temperature: float = 0.65
    llm_top_p: float = 0.92
    
    # CORS
    cors_origins: str = "*"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
