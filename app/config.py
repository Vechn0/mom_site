import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY","default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False