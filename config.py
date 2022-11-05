"""App configuration."""
from os import environ, path

import redis
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Config
    FLASK_APP = "wsgi.py"
    FLASK_ENV = "production"
    SECRET_KEY = "mysecretKey"

    # Flask-Session
    # REDIS_URI = "mysql+pymysql://localhost:3306/flask_app"
    # SESSION_TYPE = "redis"
    # SESSION_REDIS = redis.from_url(REDIS_URI)

    # Flask-Assets
    LESS_BIN = "lessc"
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = True

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
