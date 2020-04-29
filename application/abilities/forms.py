from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, BooleanField, TextAreaField, SelectField, validators
from application._init_ import damagetypes

class AbilityForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2), validators.Length(max=40), validators.optional()])
    description = TextAreaField("Description", [validators.Length(max=10000)])
    toHit = IntegerField("To Hit", [validators.optional()])
    damageFormula = StringField("Formula", [validators.Length(max=40), validators.optional()])
    damageFormula2 = StringField("Formula", [validators.Length(max=40), validators.optional()])
    damageType = SelectField(u"Damage Type", choices=damagetypes, coerce=int)
    damageType2 = SelectField(u"Damage Type", choices=damagetypes, coerce=int)
    attack = BooleanField("Attack", [validators.optional()])
    attack2 = BooleanField("Second roll", [validators.optional()])

    class Meta:
        csrf = False