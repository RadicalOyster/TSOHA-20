from flask import redirect, render_template, request, url_for

from application._init_ import app, db, login_required
from application.creatures.models import Creature
from application.creatures.forms import CreatureForm
from application.creatures.forms import CreatureEditForm
from application.auth.models import User

@app.route("/creatures/")
def creature_index():
    return render_template("creatures/list.html", creatures=(Creature.query.all()))


@app.route("/creatures/new")
@login_required(role="ADMIN")
def creature_form():
    return render_template("creatures/new.html", form = CreatureForm())

@app.route("/creatures/new", methods=["POST"])
@login_required(role="ADMIN")
def creatures_create():
    form = CreatureForm(request.form)

    if not form.validate():
        print(form.errors)
        return render_template("creatures/new.html", form = form)
        
    arguments = request.form.to_dict()
    print(arguments)

    name = arguments["name"]
    hp = arguments["hp"]
    formula = arguments["formula"]
    ac = arguments["ac"]
    speed = arguments["speed"]
    flyspeed = arguments["flyspeed"]
    swimspeed = arguments["swimspeed"]
    strength = arguments["strength"]
    dex = arguments["dex"]
    con = arguments["con"]
    intelligence = arguments["intelligence"]
    wis = arguments["wis"]
    cha = arguments["cha"]
    cr = arguments["cr"]
    proficiency = arguments["proficiency"]

    if "strsav" in arguments:
        strsav = True
    else:
        strsav = False

    if "dexsav" in arguments:
        dexsav = True
    else:
        dexsav = False
    
    if "consav" in arguments:
        consav = True
    else:
        consav = False
    
    if "intsav" in arguments:
        intsav = True
    else:
        intsav = False
    
    if "wissav" in arguments:
        wissav = True
    else:
        wissav = False
    
    if "chasav" in arguments:
        chasav = True
    else:
        chasav = True
    
    if "athletics" in arguments:
        athletics = True
    else:
        athletics = False
    
    if "acrobatics" in arguments:
        acrobatics = True
    else:
        acrobatics = False
    
    if "soh" in arguments:
        soh = True
    else:
        soh = False

    if "stealth" in arguments:
        stealth = True
    else:
        stealth = False
    
    if "arcana" in arguments:
        arcana = True
    else:
        arcana = False
    
    if "history" in arguments:
        history = True
    else:
        history = False
    
    if "investigation" in arguments:
        investigation = True
    else:
        investigation = False
    
    if "nature" in arguments:
        nature = True
    else:
        nature = False
    
    if "religion" in arguments:
        religion = True
    else:
        religion = False
    
    if "animal" in arguments:
        animal = True
    else:
        animal = False
    
    if "insight" in arguments:
        insight = True
    else:
        insight = False
    
    if "medicine" in arguments:
        medicine = True
    else:
        medicine = False
    
    if "perception" in arguments:
        perception = True
    else:
        perception = False
    
    if "surival" in arguments:
        survival = True
    else:
        survival = False
    
    if "deception" in arguments:
        deception = True
    else:
        deception = False
    
    if "intimidation" in arguments:
        intimidation = True
    else:
        intimidation = False
    
    if "performance" in arguments:
        performance = True
    else:
        performance = False
    
    if "persuasion" in arguments:
        persuasion = True
    else:
        persuasion = False

    creature = Creature(name, hp, formula, ac, speed, swimspeed, flyspeed, strength, dex, con, intelligence, wis, cha, strsav, dexsav, consav, intsav, wissav, chasav, cr,
    proficiency, athletics, acrobatics, soh, stealth, arcana, history, investigation, nature, religion, animal, insight, medicine, perception, survival, deception, intimidation,
    performance, persuasion)

    db.session().add(creature)
    db.session().commit()
    return redirect(url_for("creature_index"))

@app.route("/creatures/<creature_id>/", methods=["GET"])
def show_creature(creature_id):
    creature = Creature.query.get(creature_id)
    if creature is not None:
        return render_template("creatures/show.html", creature=creature, skills=creature.getProficiencies(), saves=creature.getSavingThrows(), form=CreatureEditForm())
    return redirect(url_for("creature_index"))


@app.route("/creatures/<creature_id>/", methods=["POST"])
def change_creature_stats(creature_id):
    form = CreatureEditForm(request.form)
    creature = Creature.query.get(creature_id)

    if not form.validate():
        return render_template("creatures/show.html", creature=Creature.query.filter_by(id=creature_id).first(), skills=creature.getProficiencies(), form=form)

    arguments = request.form.to_dict()
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

    if "strsav" in arguments:
        creature.strsav = True
    else:
        creature.strsav = False

    if "dexsav" in arguments:
        creature.dexsav = True
    else:
        creature.dexsav = False
    
    if "consav" in arguments:
        creature.consav = True
    else:
        creature.consav = False
    
    if "intsav" in arguments:
        creature.intsav = True
    else:
        creature.intsav = False
    
    if "wissav" in arguments:
        creature.wissav = True
    else:
        creature.wissav = False
    
    if "chasav" in arguments:
        creature.chasav = True
    else:
        creature.chasav = True
    
    if "athletics" in arguments:
        creature.athletics = True
    else:
        creature.athletics = False
    
    if "acrobatics" in arguments:
        creature.acrobatics = True
    else:
        creature.acrobatics = False
    
    if "soh" in arguments:
        creature.soh = True
    else:
        creature.soh = False

    if "stealth" in arguments:
        creature.stealth = True
    else:
        creature.stealth = False
    
    if "arcana" in arguments:
        creature.arcana = True
    else:
        creature.arcana = False
    
    if "history" in arguments:
        creature.history = True
    else:
        creature.history = False
    
    if "investigation" in arguments:
        creature.investigation = True
    else:
        creature.investigation = False
    
    if "nature" in arguments:
        creature.nature = True
    else:
        creature.nature = False
    
    if "religion" in arguments:
        creature.religion = True
    else:
        creature.religion = False
    
    if "animal" in arguments:
        creature.animal = True
    else:
        creature.animal = False
    
    if "insight" in arguments:
        creature.insight = True
    else:
        creature.insight = False
    
    if "medicine" in arguments:
        creature.medicine = True
    else:
        creature.medicine = False
    
    if "perception" in arguments:
        creature.perception = True
    else:
        creature.perception = False
    
    if "surival" in arguments:
        creature.survival = True
    else:
        creature.survival = False
    
    if "deception" in arguments:
        creature.deception = True
    else:
        creature.deception = False
    
    if "intimidation" in arguments:
        creature.intimidation = True
    else:
        creature.intimidation = False
    
    if "performance" in arguments:
        creature.performance = True
    else:
        creature.performance = False
    
    if "persuasion" in arguments:
        creature.persuasion = True
    else:
        creature.persuasion = False
    
    db.session().commit()

    return redirect(url_for("show_creature", creature_id=creature_id))

@app.route("/creatures/delete/<creature_id>/", methods=["POST"])
@login_required
def delete_creature(creature_id):
    creature = Creature.query.get(creature_id)
    db.session().delete(creature)
    db.session().commit()
    return redirect(url_for("creature_index"))