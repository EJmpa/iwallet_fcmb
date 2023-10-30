# config/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://ejmpa:454500@localhost/iwallet_dummy_data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
