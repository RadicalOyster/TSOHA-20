from application._init_ import db

class Ability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    attacks = db.relationship("Attack")
    creature = db.relationship("Creature", secondary="Creature_Ability")
    toHit = db.Column(db.Integer, nullable=False)

class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ability_id = db.Column(db.Integer, db.ForeignKey('ability.id'))
    ability = db.relationship("Ability", back_populates="attacks")
    damageFormula = db.Column(db.String(40), nullable=False)
    damagetype_id = db.Column(db.Integer, db.ForeignKey('damage_type.id'))
    damagetype = db.relationship("DamageType", back_populates="attacksoftype")

class DamageType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(40), nullable=False)
    attacksoftype = db.relationship("Attack", back_populates="damagetype")
