import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=c630779b624b4945b21a0972504a9607'
    NEWS_API_KEY = os.environ.get('c630779b624b4945b21a0972504a9607')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}