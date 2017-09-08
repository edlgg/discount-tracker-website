from flask import Blueprint

user_blueprint = Blueprint('stores', __name__)


@user_blueprint.route('/store/<string:name>')
def store_page():
	pass
