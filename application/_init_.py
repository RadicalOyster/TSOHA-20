from flask import Flask
app = Flask(__name__)

#load static files
app.static_folder = 'static'

# database connectivity and ORM
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dnd.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

userRoles = []

# roles in login_required
from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()
            acceptable_roles = ["ANY"]
            for userRole in current_user.roles:
                acceptable_roles.append(userRole.name)
            userRoles = acceptable_roles      
            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

from application import views

from application.creatures import models
from application.auth.models import User, Role
from application.auth import views
from application.abilities.models import DamageType

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
    Role.initialize_roles()
    User.initialize_admin()
    DamageType.initialize_damagetypes()

except:
    pass

damagetypes = []
types = DamageType.query.order_by(DamageType.type).all()
for dtype in types:
    choice = (dtype.id, dtype.type)
    damagetypes.append(choice)

from application.creatures import views
from application.auth.forms import LoginForm, UserEditForm