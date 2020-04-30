from application._init_ import db
from sqlalchemy.sql import text


class Ability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(10000), nullable=False)
    attacks = db.relationship("Attack")
    toHit = db.Column(db.Integer, nullable=False)

    def __init__(self, name, description, toHit=0):
        self.name = name
        self.description = description
        self.toHit = toHit
        self.attacks = []


class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ability_id = db.Column(db.Integer, db.ForeignKey('ability.id'))
    ability = db.relationship("Ability", back_populates="attacks")
    damageFormula = db.Column(db.String(40), nullable=False)
    damagetype_id = db.Column(db.Integer, db.ForeignKey('damage_type.id'))
    damageType = db.relationship("DamageType", back_populates="attacksoftype")

    def __init__(self, damageFormula, damagetype_id):
        self.damageFormula = damageFormula
        self.damagetype_id = damagetype_id


class DamageType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(40), nullable=False, unique=True)
    attacksoftype = db.relationship("Attack", back_populates="damageType")

    @staticmethod
    def initialize_damagetypes():
        try:
            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Acid')")
            db.engine.execute(stmt)

            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Bludgeoning')")
            db.engine.execute(stmt)

            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Cold')")
            db.engine.execute(stmt)

            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Fire')")
            db.engine.execute(stmt)

            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Force')")
            db.engine.execute(stmt)

            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Lightning')")
            db.engine.execute(stmt)
            
            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Necrotic')")
            db.engine.execute(stmt)

            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Piercing')")
            db.engine.execute(stmt)
            
            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Poison')")
            db.engine.execute(stmt)

            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Psychic')")
            db.engine.execute(stmt)
            
            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Radiant')")
            db.engine.execute(stmt)

            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Slashing')")
            db.engine.execute(stmt)
            
            stmt = text("INSERT INTO Damage_Type (type) VALUES ('Thunder')")
            db.engine.execute(stmt)
        except:
            pass