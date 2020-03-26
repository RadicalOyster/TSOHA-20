from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, validators

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
    cr = DecimalField("CR")

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