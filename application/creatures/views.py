from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application._init_ import app, db
from application.creatures.models import Creature
from application.creatures.forms import CreatureForm
from application.creatures.forms import CreatureEditForm

@app.route("/creatures/")
def creature_index():
    return render_template("creatures/list.html", creatures=(Creature.query.all()))


@app.route("/creatures/new")
@login_required
def creature_form():
    return render_template("creatures/new.html", form = CreatureForm())

@app.route("/creatures/<creature_id>/", methods=["GET"])
def show_creature(creature_id):
    creature = Creature.query.get(creature_id)
    if creature is not None:
        return render_template("creatures/show.html", creature=creature, form=CreatureEditForm())
    return redirect(url_for("creature_index"))


@app.route("/creatures/<creature_id>/", methods=["POST"])
def change_creature_stats(creature_id):
    form = CreatureEditForm(request.form)

    if not form.validate():
        return render_template("creatures/show.html", form=form, creature=Creature.query.filter_by(id=creature_id).first())

    creature = Creature.query.get(creature_id)
    name = request.form.get('name')
    hp = request.form.get('hp')
    formula = request.form.get('formula')
    ac = request.form.get('ac')
    speed = request.form.get('speed')
    flyspeed = request.form.get('flyspeed')
    swimspeed = request.form.get('swimspeed')
    strength = request.form.get('strength')
    dex = request.form.get('dex')
    con = request.form.get('con')
    intelligence = request.form.get('intelligence')
    wis = request.form.get('wis')
    cha = request.form.get('cha')
    cr = request.form.get('cr')

    if name is not '':
        creature.name = name
    if hp is not '':
        creature.hp = hp
    if formula is not '':
        creature.formula = formula
    if ac is not '':
        creature.ac = ac
    if speed is not '':
        creature.speed = speed
    if swimspeed is not '':
        creature.swimspeed = swimspeed
    if flyspeed is not '':
        creature.flyspeed = flyspeed
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
    if cr is not '':
        creature.cr = cr
    
    db.session().commit()

    return redirect(url_for("show_creature", creature_id=creature_id))

@app.route("/creatures/delete/<creature_id>/", methods=["POST"])
@login_required
def delete_creature(creature_id):
    creature = Creature.query.get(creature_id)
    db.session().delete(creature)
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
