from flask import render_template
from application._init_ import app

@app.route("/")
def index():
    return render_template("index.html")