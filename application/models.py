from datetime import datetime
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from flask_login import UserMixin
from application import (
    db,
    login
)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'User {self.username}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_text = db.Column(db.String(256))
    date_added = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    team_id = db.Column(db.String(16), index=True)
    team_domain = db.Column(db.String(64), index=True)
    user_added = db.Column(db.String(16), index=True)
    user_posted = db.Column(db.String(16), index=True)
    ts_posted = db.Column(db.String(32))
    channel = db.Column(db.String(16), index=True)
    replies = db.Column(db.Integer, index=True, nullable=True)

    # def __repr__(self):
    #     return f'Post {self.team_domain}'


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.String(30))
    user_id = db.Column(db.String(30))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    token = db.Column(db.String(120))
