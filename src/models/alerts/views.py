from flask import Blueprint

user_blueprint = Blueprint('alerts', __name__)


@user_blueprint.route('/new', methods=['POST'])
def create_alert():
	pass

@user_blueprint.route('/deactivate/<string:alert_id>')
def deactivate_alert(alert_id):
	pass

@user_blueprint.route('/alert/<string:alert_id>')
def get_alert_page(alert_id):
	pass

@user_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
	pass
	