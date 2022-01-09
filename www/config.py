"""Flask configuration."""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

TESTING = True
DEBUG = True

# Flask
# FLASK_APP = 'wsgi.py'
FLASK_ENV = 'development'
SECRET_KEY = 'htkpm5Oswy6ncp69xjuywzklopm52'

# Database
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Application
UPLOAD_FOLDER = '/home/mzfkjug/upload'
