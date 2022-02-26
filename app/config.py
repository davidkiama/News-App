

class Config:
    '''
    Global configuration of the parent
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


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
