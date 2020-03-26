from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, validators

class CreatureForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    hp = IntegerField("HP", [validators.NumberRange(min=1)])
    formula = StringField("HP formula")
    ac = IntegerField("AC", [validators.NumberRange(min=0)])
    speed = IntegerField("Speed", [validators.NumberRange(min=0)])
    flyspeed = IntegerField("Flying speed", [validators.NumberRange(min=0)])
    swimspeed = IntegerField("Swimming speed", [validators.NumberRange(min=0)])
    strength = IntegerField("STR", [validators.NumberRange(min=1)])
    dex = IntegerField("DEX", [validators.NumberRange(min=1)])
    con = IntegerField("CON", [validators.NumberRange(min=1)])
    intelligence = IntegerField("INT", [validators.NumberRange(min=1)])
    wis = IntegerField("WIS", [validators.NumberRange(min=1)])
    cha = IntegerField("CHA", [validators.NumberRange(min=1)])
    cr = DecimalField("CR")

    class Meta:
        csrf = False