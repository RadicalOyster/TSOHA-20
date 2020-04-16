from application._init_ import db

class AttackDamageType(db.Model):
   __tablename__ = "Attack_DamageType"
   id = db.Column(db.Integer, primary_key=True)
   attack_id = db.Column(db.Integer, db.ForeignKey('attack.id'))
   damagetype_id = db.Column(db.Integer, db.ForeignKey('damage_type.id'))

class Ability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    attack_id = db.Column(db.Integer, db.ForeignKey('attack.id'))
    attack = db.relationship("Attack", uselist=False, backref="ability")
    creature = db.relationship("Creature", secondary="Creature_Ability")

class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    damageFormula = db.Column(db.String(40), nullable=False)
    toHit = db.Column(db.Integer, nullable=False)
    damageType = db.relationship("DamageType", secondary="Attack_DamageType", backref='damage_type')

class DamageType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(40), nullable=False)
    attack = db.relationship("Attack", secondary="Attack_DamageType")