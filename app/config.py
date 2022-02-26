class Config:
    '''
    Global configuration of the parent
    '''


class ProdConfig(Config):
    '''
    Production configuration child
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child
    '''
    DEBUG = True
