from flask import Flask, render_template
from common.database import Database

__author__ = "edlgg"

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123"

@app.before_first_request
def init_db():
	Database.initialize()

@app.route('/')
def home():
    return render_template('home.jinja2')

from models.users.views import user_blueprint
from models.alerts.views import alert_blueprint
from models.stores.views import store_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
