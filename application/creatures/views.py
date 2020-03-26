from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application._init_ import app, db
from application.creatures.models import Creature
from application.creatures.forms import CreatureForm


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/creatures/")
def creature_index():
    return render_template("creatures/list.html", creatures=(Creature.query.all()))


@app.route("/creatures/new")
@login_required
def creature_form():
    return render_template("creatures/new.html", form = CreatureForm())

@app.route("/creatures/<creature_id>/", methods=["GET"])
def show_creature(creature_id):
    print("THIS IS POOOOOARTOAEOTAEOTAEOTO\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa\naaaa")
    if int(creature_id) <= len(Creature.query.all()):
        return render_template("creatures/show.html", creature=(Creature.query.filter_by(id=creature_id).first()))
    return redirect(url_for("creature_index"))


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
    form = CreatureForm(request.form)

    if not form.validate():
        return render_template("creatures/new.html", form = form)
        
    arguments = request.form.to_dict().values()
    print(arguments)
    creature = Creature(*arguments)
    db.session().add(creature)
    db.session().commit()
    return redirect(url_for("creature_index"))
