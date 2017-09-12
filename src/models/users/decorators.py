from functools import wraps
from flask import request, session, url_for
from werkzeug.utils import redirect

def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return redirect(url_for('users.login_user'), next=request.path)
        return func(*args, **kwargs)
    return decorated_function

@requires_login
def my_function(x,y):
    return x+y