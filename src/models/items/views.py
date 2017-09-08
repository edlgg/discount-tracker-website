from flask import Blueprint

user_blueprint = Blueprint('items', __name__)


@user_blueprint.route('/item/<string:name>')
def item_page(name):
	pass


