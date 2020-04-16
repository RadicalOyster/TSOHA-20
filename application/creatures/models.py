from application._init_ import db
from sqlalchemy.sql import text

class CreatureAbility(db.Model):
   __tablename__ = "Creature_Ability"
   id = db.Column(db.Integer, primary_key=True)
   creature_id = db.Column(db.Integer, db.ForeignKey('creature.id'))
   ability_id = db.Column(db.Integer, db.ForeignKey('ability.id'))

class Creature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    formula = db.Column(db.String(40))
    ac = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer)
    swimspeed = db.Column(db.Integer)
    flyspeed = db.Column(db.Integer)
    cr = db.Column(db.String(20))
    str = db.Column(db.Integer, nullable=False)
    dex = db.Column(db.Integer, nullable=False)
    con = db.Column(db.Integer, nullable=False)
    int = db.Column(db.Integer, nullable=False)
    wis = db.Column(db.Integer, nullable=False)
    cha = db.Column(db.Integer, nullable=False)
    abilities = db.relationship("Ability", secondary="Creature_Ability", backref='ability')

    def __init__(self, name, hp, formula, ac, speed, swimspeed, flyspeed, strength, dex, con, intelligence, wis, cha, cr):
        self.name = name
        self.hp = hp
        self.formula = formula
        self.ac = ac
        self.speed = speed
        self.swimspeed = swimspeed
        self.flyspeed = flyspeed
        self.str = strength
        self.dex = dex
        self.con = con
        self.int = intelligence
        self.wis = wis
        self.cha = cha
        self.cr = str(cr)
    
    @staticmethod
    def find_creatures_with_damage_type(damagetype=''):
        stmt = text("SELECT Creature.id, Creature.name FROM Creature"
                    " LEFT JOIN Creature_Ability ON Creature.id = Creature_Ability.creature_id"
                    " LEFT JOIN Ability ON Ability.id = Creature_Ability.ability_id"
                    " LEFT JOIN Attack ON Attack.id = Ability.attack_id"
                    " LEFT JOIN Attack_DamageType ON Attack.id = Attack_DamageType.attack_id"
                    " LEFT JOIN Damage_Type ON Damage_Type.id = Attack_DamageType.damagetype_id"
                    " WHERE Damage_Type.type = :damagetype").params(damagetype=damagetype)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
            
        return response