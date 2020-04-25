from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class SignupForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=40)])
    username = StringField("Username", [validators.Length(min=2, max=40)])
    password = PasswordField("Password", [validators.Length(min=4, max=40), validators.EqualTo("repeat", message="Passwords must match")])
    repeat = PasswordField("Repeat", [validators.Length(min=4, max=40)])

    class Meta:
        csrf = False

class UserEditForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False