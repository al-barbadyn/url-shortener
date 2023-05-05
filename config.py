import os

from dotenv import load_dotenv


load_dotenv()


class DatabaseConfig:
	DB_URI: str = os.environ.get("DB_URI", "postgresql://postgres:postgres@localhost:5432/url_shortener")


class BaseConfig(DatabaseConfig):
	DEBUG: bool = os.environ.get("DEBUG", False)
	URL_LENGTH: int = os.environ.get("URL_LENGTH", 6)


config = BaseConfig()
