import os


class Config:
    DEBUG = os.environ.get('DEBUG', True)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = 'postgres://ikfksipvumzrgj:a3ba740d3b23d6b9e8cca63ab62894ddcbac20fd1979b4c2b1fe0ec834340b3a@ec2-50-17-90-177.compute-1.amazonaws.com:5432/d5hjj38tvdpi60' #os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CONTACT_SUBJECT = 'Message from your site.'
