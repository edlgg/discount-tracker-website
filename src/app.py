from flask import Flask
from common.database import Database

__author__ = "edlgg"

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123"

@app.before_first_request
def init_db():
	Database.initialize()

from models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
