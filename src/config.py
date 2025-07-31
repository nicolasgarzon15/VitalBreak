class Config:
    SECRET_KEY = 'Secret'


class DevelopmentConfig(Config):
    DEBUG=True
    HOST = 'ep-lingering-salad-a2ump1k5-pooler.eu-central-1.aws.neon.tech',
    USER = 'neondb_owner',
    PASSWORD = 'npg_RsXCf5J7Ltmn',
    DB = 'neondb',
    PUERTO = '5432'

config = {
    'development':DevelopmentConfig
}