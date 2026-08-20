from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- Cấu hình ứng dụng ---
    APP_NAME: str = "RESEARCH GROUP MANAGEMENT API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Research Group"

    # --- Cấu hình Database ---
    DATABASE_URL: str = "mysql+pymysql://root:452007@localhost:3306/research_db"

    # --- Cấu hình JWT ---
    SECRET_KEY: str = "4-5-2-0-0-7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # --- Cấu hình CORS ---
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:5173"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()