from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, BooleanField, validators

class CreatureForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    hp = IntegerField("HP", [validators.NumberRange(min=1)])
    formula = StringField("HP formula")
    ac = IntegerField("AC", [validators.NumberRange(min=0)])
    speed = IntegerField("Speed")
    flyspeed = IntegerField("Flying speed")
    swimspeed = IntegerField("Swimming speed")
    strength = IntegerField("STR", [validators.NumberRange(min=1)])
    dex = IntegerField("DEX", [validators.NumberRange(min=1)])
    con = IntegerField("CON", [validators.NumberRange(min=1)])
    intelligence = IntegerField("INT", [validators.NumberRange(min=1)])
    wis = IntegerField("WIS", [validators.NumberRange(min=1)])
    cha = IntegerField("CHA", [validators.NumberRange(min=1)])
    proficiency = IntegerField("Proficiency", [validators.NumberRange(min=0)])
    cr = DecimalField("CR")
    strsav = BooleanField("STR")
    dexsav = BooleanField("DEX")
    consav = BooleanField("CON")
    intsav = BooleanField("INT")
    wissav = BooleanField("WIS")
    chasav = BooleanField("CHA")

    athletics = BooleanField("Athletics")
    
    acrobatics = BooleanField("Acrobatics")
    soh = BooleanField("Sleight of Hand")
    stealth = BooleanField("Stealth")

    arcana = BooleanField("Arcana")
    history = BooleanField("History")
    investigation = BooleanField("Investigation")
    nature = BooleanField("Nature")
    religion = BooleanField("Religion")

    animal = BooleanField("Animal Handling")
    insight = BooleanField("Insight")
    medicine = BooleanField("Medicine")
    perception = BooleanField("Perception")
    survival = BooleanField("Survival")

    deception = BooleanField("Deception")
    intimidation = BooleanField("Intimidation")
    performance = BooleanField("Performance")
    persuasion = BooleanField("Persuasion")

    class Meta:
        csrf = False

class CreatureEditForm(FlaskForm):
    name = StringField("Name")
    hp = IntegerField("HP")
    formula = StringField("HP formula")
    ac = IntegerField("AC")
    speed = IntegerField("Speed")
    flyspeed = IntegerField("Flying speed")
    swimspeed = IntegerField("Swimming speed")
    strength = IntegerField("STR")
    dex = IntegerField("DEX")
    con = IntegerField("CON")
    intelligence = IntegerField("INT")
    wis = IntegerField("WIS")
    cha = IntegerField("CHA")
    cr = DecimalField("CR")

    class Meta:
        csrf = False