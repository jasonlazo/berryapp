import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configuration"""
    host = '0.0.0.0'
    debug = True
    port = 8000
    reload = False
    log_level = 'debug'


class ProductionConfig(Config):
    """Production configuration"""
    host = 'globant.jasonlazolock.com'
    debug = False


class DevelopmentConfig(Config):
    """Development configuration"""
    reload = True


class TestingConfig(Config):
    """Testing configuration"""


def get_config():
    return ProductionConfig()
