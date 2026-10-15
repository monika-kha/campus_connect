
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AWS_REGION = os.environ.get("AWS_REGION", "ap-south-1")
    S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
    BACKUP_PREFIX = os.environ.get("BACKUP_PREFIX", "backups/db/")

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
