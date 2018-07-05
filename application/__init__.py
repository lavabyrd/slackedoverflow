from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

import os


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# when I start the db work, I can use this start the migration
# migrate = Migrate(app, db)


from application import routes
