import os
try:
    import local_config
except:
    pass

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    VERIFICATION_TOKEN = os.environ.get(
        "SO_VERIFICATION_TOKEN") or local_config.veri
    BOT_TOKEN = os.environ.get("SO_TOKEN") or local_config.bot_token
    USER_TOKEN = os.environ.get("SO_USER_TOKEN") or local_config.user_token
    OAUTH_SCOPE = os.environ.get("SCOPES") or local_config.scopes
    CLIENT_ID = os.environ.get("CLIENT_ID") or local_config.client_id
    CLIENT_SECRET = os.environ.get(
        "CLIENT_SECRET") or local_config.client_secret
    USER_TOKEN = os.environ.get("SO_USER_TOKEN") or local_config.user_token
