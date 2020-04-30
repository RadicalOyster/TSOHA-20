from flask import redirect, render_template, request, url_for
from application._init_ import app, db


@app.route("/")
def index():
    return render_template("index.html")