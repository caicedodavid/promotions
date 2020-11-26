import os


class BaseConfig:
    """ Base configuration """
    TESTING = False
    DEBUG = True
    MONGODB_HOST = os.environ.get('MONGODB_HOST')


class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(BaseConfig):
    """ Testing configuration """
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = f'{os.environ.get("DATABASE_URL")}_test'


class StagingConfig(BaseConfig):
    """ Staging configuration """
    pass


class ProductionConfig(BaseConfig):
    """ Production configuration """
    DEBUG = False
