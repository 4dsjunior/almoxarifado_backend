import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./almoxarifado.db")
