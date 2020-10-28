import os


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'chaveteste')
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = '\xb1p2\xebc\x962Rx\x02\xe1\x86\x9fOC\xea,J[F\xc3\xf4-'
    DEBUG = False
