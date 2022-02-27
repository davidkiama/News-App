
import os


class Config:
    '''
    Global configuration of the parent
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    print('1111111111111111111111111111111111111111111111111111111111111111111111111')
    print(NEWS_API_KEY)
    SECRET_KEY = os.environ.get('SECRET_KEY')


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


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
