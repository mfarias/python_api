import os


class Config:

    # General Config
    TESTING = True
    DEBUG = True

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql+psycopg2://postgres:postgres@localhost:5432/user_api')
    SQLALCHEMY_USERNAME = 'postgres'
    SQLALCHEMY_PASSWORD = 'postgres'
    SQLALCHEMY_DATABASE_NAME = 'user_api'
    SQLALCHEMY_TABLE = 'migrations'
    SQLALCHEMY_DB_SCHEMA = 'public'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
