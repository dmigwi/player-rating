class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False

class TestConfiguration(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
