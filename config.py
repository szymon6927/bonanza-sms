class Config:
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SECRET_KEY = '64611845097b83af8c787f73'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
