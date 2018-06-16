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
