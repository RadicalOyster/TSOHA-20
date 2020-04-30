from flask import redirect, render_template, request, url_for

from application._init_ import app, db, login_required, current_user
from application.creatures.models import Creature
from application.creatures.forms import CreatureForm, CreatureEditForm, creatureSearchForm
from application.abilities.models import DamageType, Ability, Attack
from application.abilities.forms import AbilityForm
from application.auth.models import User

# List creatures
@app.route("/creatures/", methods=["GET", "POST"])
def creature_index():

    if request.method == "POST":
        form = creatureSearchForm(request.form)

        if request.form.get("nameButton") is not None:
            return redirect(url_for("search_by_name", creature_name=request.form.get("name")))
        elif request.form.get("damageTypeButton") is not None:
            return redirect(url_for("search_by_damage_type", damage_type_id=request.form.get("damageType")))

    return render_template("creatures/list.html", creatures=(Creature.query.all()), searchForm=creatureSearchForm())


# Search for creature by name
@app.route("/creatures/search/name/<creature_name>")
def search_by_name(creature_name):
    filterstring = "%"
    filterstring += (creature_name + "%")
    creatures = Creature.query.filter(Creature.name.like(filterstring)).all()
    return render_template("creatures/list.html", creatures=creatures, searchForm=creatureSearchForm())


# Search for creature by damage type
@app.route("/creatures/search/damagetype/<damage_type_id>", methods=["GET"])
def search_by_damage_type(damage_type_id):
    return render_template("creatures/list.html", creatures=Creature.find_creatures_with_damage_type(damage_type_id), searchForm=creatureSearchForm())


# List a user's favorites
@app.route("/creatures/favorites")
@login_required(role="USER")
def list_favorites():
    return render_template("creatures/favorites.html", creatures=current_user.creatures)

# Template for new creature
@app.route("/creatures/new")
@login_required(role="ADMIN")
def creature_form():
    return render_template("creatures/new.html", form=CreatureForm())

# Adding new creature to the database
@app.route("/creatures/new", methods=["POST"])
@login_required(role="ADMIN")
def creatures_create():
    form = CreatureForm(request.form)

    if not form.validate():
        print(form.errors)
        return render_template("creatures/new.html", form=form)

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

# Show detailed creature info
@app.route("/creatures/<creature_id>/", methods=["GET"])
def show_creature(creature_id):
    creature = Creature.query.get(creature_id)
    favorite = False
    if current_user.is_authenticated and creature in current_user.creatures:
        favorite = True
    if creature is not None:
        return render_template("creatures/show.html", creature=creature, skills=creature.getProficiencies(), saves=creature.getSavingThrows(), form=CreatureEditForm(), abilityForm=AbilityForm(), favorite=favorite)
    return redirect(url_for("creature_index"))

# View and edit creature ability
@app.route("/creatures/<creature_id>/<ability_id>", methods=["GET"])
@login_required(role="ADMIN")
def creature_ability(creature_id, ability_id):
    form = AbilityForm()
    creature = Creature.query.get(creature_id)
    ability = Ability.query.get(ability_id)
    attack = {"damageType": '', "damageFormula": ''}
    attack2 = {"damageType": '', "damageFormula": ''}
    attacks = ability.attacks

    print("\n\n\n")
    print(form.damageType)
    print("\n\n\n")

    try:
        attack = attacks[0]
        form.damageType.default = attack.damageType.id
        form.process()
    except:
        pass
    try:
        attack2 = attacks[1]
        form.damageType2.default = attack2.damageType.id
        form.process()
    except:
        pass
    return render_template("creatures/ability.html", creature=creature, ability=ability, attack=attack, attack2=attack2, abilityForm=form)

# Update ability in the database
@app.route("/creatures/<creature_id>/<ability_id>", methods=["POST"])
@login_required(role="ADMIN")
def update_creature_ability(creature_id, ability_id):
    form = AbilityForm(request.form)
    ability = Ability.query.get(ability_id)

    if not form.validate():
        return render_template("creatures/ability.html", creature=Creature.query.get(creature_id), ability=ability, abilityForm=form)

    ability.name = request.form.get("name")
    ability.descrpition = request.form.get("description")
    ability.toHit = request.form.get("toHit")

    isattack1 = request.form.get("attack")
    isattack2 = request.form.get("attack2")

    damage1 = request.form.get("damageFormula")
    damage2 = request.form.get("damageFormula2")

    damageType1 = form.damageType.data
    damageType2 = form.damageType2.data

    attacks = ability.attacks
    newattacks = []

    newattack1 = Attack(damage1, damageType1)
    newattack2 = Attack(damage2, damageType2)

    if len(attacks) is 0 and isattack1 is 'y':
        newattacks.append(newattack1)
        if isattack2 is 'y':
            newattacks.append(newattack2)

    elif len(attacks) is 1 and isattack2 is 'y':
        attack2 = Attack(damage2, damageType2)
        newattacks.append(newattack1)
        newattacks.append(newattack2)

    elif isattack1 is not 'y':
        newattacks = []

    elif isattack2 is not 'y':
        newattacks.append(newattack1)

    db.session().commit()

    return redirect(url_for("update_creature_ability", creature_id=creature_id, ability_id=ability_id))

# Add new ability to creature
@app.route("/creatures/<creature_id>/ability", methods=["POST"])
@login_required(role="ADMIN")
def add_ability(creature_id):
    form = AbilityForm(request.form)
    creature = Creature.query.get(creature_id)

    if not form.validate():
        return render_template("creatures/show.html", creature=creature, skills=creature.getProficiencies(), saves=creature.getSavingThrows(), form=CreatureEditForm(), abilityForm=form)

    name = request.form.get("name")
    description = request.form.get("description")
    ability = Ability(name, description, request.form.get("toHit"))

    print(request.form.get("attack"))
    print(request.form.get("attack2"))

    isattack = request.form.get("attack")
    isattack2 = request.form.get("attack2")

    if isattack is 'y':
        damage = request.form.get("damageFormula")
        damagetype = form.damageType.data
        newattack1 = Attack(damage, damagetype)
        ability.attacks.append(newattack1)
        if isattack2 is 'y':
            damage2 = request.form.get("damageFormula2")
            damagetype2 = form.damageType2.data
            newattack2 = Attack(damage2, damagetype2)
            ability.attacks.append(attack2)
        else:
            pass
    else:
        pass

    creature.abilities.append(ability)

    db.session().add(creature)
    db.session().commit()

    return redirect(url_for("show_creature", creature_id=creature_id))


# Update creature stats
@app.route("/creatures/<creature_id>/", methods=["POST"])
@login_required(role="ADMIN")
def change_creature_stats(creature_id):
    form = CreatureEditForm(request.form)
    creature = Creature.query.get(creature_id)

    if not form.validate():
        return render_template("creatures/show.html", creature=Creature.query.filter_by(id=creature_id).first(), skills=creature.getProficiencies(), form=form, abilityForm=AbilityForm())

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
    proficiency = request.form.get('proficiency')

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
    if proficiency is not '':
        creature.proficiency = proficiency

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

# delete creature
@app.route("/creatures/delete/<creature_id>/", methods=["POST"])
@login_required
def delete_creature(creature_id):
    creature = Creature.query.get(creature_id)
    db.session().delete(creature)
    db.session().commit()
    return redirect(url_for("creature_index"))

# add creature to user's favorites
@app.route("/creatures/favorite/<creature_id>", methods=["POST"])
@login_required
def favorite_creature(creature_id):
    user = User.query.get(request.form["user_id"])
    creature = Creature.query.get(creature_id)
    user.creatures.append(creature)
    db.session.commit()
    return redirect(url_for("show_creature", creature_id=creature_id))

# remove creature from user's favorites
@app.route("/creatures/favorite/<creature_id>/remove", methods=["POST"])
@login_required
def remove_favorite(creature_id):
    user = User.query.get(request.form["user_id"])
    creature = Creature.query.get(creature_id)
    user.creatures.remove(creature)
    db.session.commit()
    return redirect(url_for("show_creature", creature_id=creature_id))
