from decouple import config

class Config: # interactuar con la variable de entorno
    SECRET_KEY=config('SECRET_KEY')

class DevelopmentConfig(Config): # modo depuración activo
    DEBUG = True

config = {
    'development':DevelopmentConfig
}