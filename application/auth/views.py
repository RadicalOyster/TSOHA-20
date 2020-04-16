from flask import render_template, request, redirect, request, url_for
from flask_login import login_user, logout_user
  
from application._init_ import app, login_required, db
from application.auth.models import User
from application.auth.forms import LoginForm, UserEditForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/admin")
@login_required(role="ADMIN")
def admin_panel():
    return render_template("auth/adminpanel.html", users=User.query.all())

@app.route("/auth/admin/user/<user_id>/")
@login_required(role="ADMIN")
def user_view(user_id):
    return render_template("auth/viewuser.html", user=User.query.get(user_id), form=UserEditForm())

@app.route("/auth/admin/user/<user_id>/", methods=["POST"])
@login_required(role="ADMIN")
def update_user(user_id):
    form = UserEditForm(request.form)

    if not form.validate():
        return render_template("auth/viewuser.html", form=form, user=User.query.get(user_id))

    user = User.query.get(user_id)

    print("\n\n\n\n\n\n\n\n")
    print(user.name)
    print(user.username)
    print(user.password)
    print("\n\n\n\n\n\n\n\n")

    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    if name is not '':
        user.name = name
    if username is not '':
        user.username = username
    if password is not '':
        user.password = password

    db.session().add(user)
    db.session().commit()
    
    return redirect(url_for("user_view", user_id=user_id))

@app.route("/auth/admin/user/delete/<user_id>/", methods=["POST"])
@login_required(role="ADMIN")
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session().delete(user)
    db.session().commit()
    return redirect(url_for("admin_panel"))