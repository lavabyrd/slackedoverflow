import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # Set to false as not needed to notify the app when a db
    # change is put in place
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    VERIFICATION_TOKEN = os.environ.get(
        "SO_VERIFICATION_TOKEN")
    BOT_TOKEN = os.environ.get("SO_TOKEN")
    USER_TOKEN = os.environ.get("SO_USER_TOKEN")
    OAUTH_SCOPE = os.environ.get("SCOPES")
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get(
        "CLIENT_SECRET")
    USER_TOKEN = os.environ.get("SO_USER_TOKEN")
