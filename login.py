from functools import wraps
from flask import redirect, render_template, request, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("uname") is None:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function