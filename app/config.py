import os


class Config:
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONTACT_SUBJECT = 'Message from your site.'
