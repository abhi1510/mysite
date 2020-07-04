import os


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONTACT_SUBJECT = 'Message from your site.'
    ADMIN_USER = os.environ.get('ADMIN_USER')
    ADMIN_PASS = os.environ.get('ADMIN_PASS')

    print(SECRET_KEY, SQLALCHEMY_DATABASE_URI, ADMIN_USER, ADMIN_PASS)
