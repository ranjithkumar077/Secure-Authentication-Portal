import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'softgrowtech_super_secret_key_2026'
    # Use absolute path for sqlite database
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database', 'users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
