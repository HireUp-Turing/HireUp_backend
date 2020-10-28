import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# allows us to make use of .env file with os.getenv
# override=True overrides System environment variables
load_dotenv(override=True)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'really hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_DEV')

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST')

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_DEV')
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_PROD')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
