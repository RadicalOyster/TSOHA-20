from flask import redirect, render_template, request, url_for
from application._init_ import app, db
from application.creatures.models import Creature


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/creatures/")
def creature_index():
    return render_template("creatures/list.html", creatures=(Creature.query.all()))


@app.route("/creatures/new")
def creature_form():
    return render_template("creatures/new.html")


@app.route("/creatures/<creature_id>/", methods=["POST"])
def change_creature_stats(creature_id):
    creature = Creature.query.get(creature_id)
    strength = request.form.get('strength')
    dex = request.form.get('dex')
    con = request.form.get('con')
    intelligence = request.form.get('intelligence')
    wis = request.form.get('wis')
    cha = request.form.get('cha')

    if strength is not '':
        creature.str = strength
    if dex is not '':
        creature.dex = dex
    if con is not '':
        creature.con = con
    if intelligence is not '':
        creature.int = intelligence
    if wis is not '':
        creature.wis = wis
    if cha is not '':
        creature.cha = cha

    db.session().commit()

    return redirect(url_for("creature_index"))


@app.route("/creatures/", methods=["POST"])
def creatures_create():
    arguments = request.form.to_dict().values()
    creature = Creature(*arguments)
    db.session().add(creature)
    db.session().commit()
    return redirect(url_for("creature_index"))
