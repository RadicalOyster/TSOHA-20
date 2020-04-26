from flask import render_template, request, redirect, request, url_for
from flask_login import login_user, logout_user

from application._init_ import app, login_required, db, current_user
from application.auth.models import User, Role
from application.auth.forms import LoginForm, UserEditForm, SignupForm, PasswordChangeForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

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


@app.route("/auth/signup/", methods=["GET"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("auth/signup.html", form=SignupForm())


@app.route("/auth/signup/", methods=["POST"])
def create_user():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = SignupForm(request.form)
    if not form.validate():
        form.password.data = ""
        form.repeat.data = ""
        return render_template("auth/signup.html", form=form)

    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    user = User(name, username, password)
    userRole = Role.find_role_by_name("USER")
    role = Role.query.get(userRole[0]["id"])
    user.roles.append(role)
    print("\n\n\n")
    print(user.roles)
    print("\n\n\n")
    db.session().add(user)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/user/<user_id>/", methods=["GET"])
@login_required(role="USER")
def show_user(user_id):
    return render_template("auth/user.html", user=User.query.get(user_id), form=PasswordChangeForm(), collapsed=True)


@app.route("/auth/user/<user_id>/", methods=["POST"])
@login_required(role="USER")
def change_password(user_id):
    form = PasswordChangeForm(request.form)
    print(form.validate())
    for i in form.errors:
        print(form.errors[i])
    if not form.validate():
        return render_template("auth/user.html", user=User.query.get(user_id), form=form, collapsed=False)
    print(user_id)
    account = User.query.get(user_id)
    account.password = request.form.get("newpassword")
    print("\n\n\n")
    print(account.name)
    print(account.username)
    print(account.password)
    print("\n\n\n")
    db.session().commit()
    return render_template("auth/loginform.html", form=LoginForm(), message="Password changed. Please login again.")