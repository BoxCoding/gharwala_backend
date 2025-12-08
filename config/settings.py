from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    #API Configuration
    api_title: str ="Gharwala API-Property consultancy Platform"
    api_description: str" India's No 1 Property consultancy Platform"
    api_version: str="1.0.0"
    api_contact_name: str="Gharwala"
    api_contact_email: str="info@gharwala.com"
    api_contact_url: str="https://www.gharwala.com"
    api_contact_phone: str="9540474247"
    api_contact_address: str="My house, my street, my city, my country"
    debug: bool=False
    HOST: str="0.0.0.0"
    PORT: int=8000

    #LLM Configuration
    llm_model: str="ollama/llama3.2:1b"
    llm_temperature: float=0.7
    llm_max_tokens: int=3000
    llm_top_p: float=1.0
    llm_frequency_penalty: float=0.0
    llm_presence_penalty: float=0.0
    llm_api_key: Optional[str]=None
    llm_api_base: str="http://localhost:11434"

    #Vector Database Configuration
    vector_database_type: str="Chroma"
    vector_database_url: str="http://localhost:8080"
    vector_database_api_key: Optional[str]=None
    vector_database_api_version: str="v1"
    vector_database_api_model: str="all-MiniLM-L6-v2"

    #PostgreSQL Configuration
    postgres_database_url: str="postgresql://postgres:postgres@localhost:5432/ghp_dwh"
    postgres_database_name: str="postgres"
    postgres_database_port: int=5432
    postgres_database_host: str="localhost"
    postgres_database_user: str="postgres"
    postgres_database_password: str="postgres"
    postgres_database_schema: str="public"
    MONGODB_URL: str="mongodb://localhost:27017/ghp_dwh"
    MONGODB_NAME: str="ghp_dwh"
    

    #Redis Configuration
    REDIS_URL: str="redis://localhost:6379/0"
    REDIS_CACHE_TTL: int=3600
    SESSION_TTL: int=7200

    #NEWS API Configuration
    NEWS_API_KEY: Optional[str]=None
    NEWS_API_BASE: str="https://newsapi.org/v2"

    #Monitoring & Logging Configuration
    LOG_LEVEL: str="INFO"
    ENABLE_MONITORING: bool=True
    PROMETHEUS_PORT: int=9090

    #Security Configuration
    CORS_ORIGINS: list[str]=["*"]
    RATE_LIMIT_REQUESTS: int=100
    RATE_LIMIT_PERIOD: int=60

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()


    