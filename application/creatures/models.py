from application._init_ import db
from sqlalchemy.sql import text


def Modifier(creature, skill):
    ret = -6
    if skill in ["STR", "Athletics"]:
        ret = int((creature.str - 10)/2)
    elif skill in ["DEX", "Acrobatics", "Sleight of Hand", "Stealth"]:
        ret = int((creature.dex - 10)/2)
    elif skill in ["INT", "Arcana", "History", "Investigation", "Nature", "Religion"]:
        ret = int((creature.int - 10)/2)
    elif skill in ["WIS", "Animal Handling", "Insight", "Medicine", "Perception", "Survival"]:
        ret = int((creature.wis - 10)/2)
    elif skill in ["CHA", "Deception", "Intimidation", "Performance", "Persuasion"]:
        ret = int((creature.cha - 10)/2)
    elif skill in ["CON"]:
        ret = int((creature.con - 10)/2)
    return ret


class CreatureAbility(db.Model):
    __tablename__ = "Creature_Ability"
    id = db.Column(db.Integer, primary_key=True)
    creature_id = db.Column(db.Integer, db.ForeignKey('creature.id'))
    ability_id = db.Column(db.Integer, db.ForeignKey('ability.id'))


class Creature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    formula = db.Column(db.String(40))
    ac = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    swimspeed = db.Column(db.Integer)
    flyspeed = db.Column(db.Integer)
    cr = db.Column(db.String(20))
    str = db.Column(db.Integer, nullable=False)
    dex = db.Column(db.Integer, nullable=False)
    con = db.Column(db.Integer, nullable=False)
    int = db.Column(db.Integer, nullable=False)
    wis = db.Column(db.Integer, nullable=False)
    cha = db.Column(db.Integer, nullable=False)
    proficiency = db.Column(db.Integer, nullable=False)
    strsav = db.Column(db.Boolean, nullable=False)
    dexsav = db.Column(db.Boolean, nullable=False)
    consav = db.Column(db.Boolean, nullable=False)
    intsav = db.Column(db.Boolean, nullable=False)
    wissav = db.Column(db.Boolean, nullable=False)
    chasav = db.Column(db.Boolean, nullable=False)

    athletics = db.Column(db.Boolean, nullable=False)

    acrobatics = db.Column(db.Boolean, nullable=False)
    soh = db.Column(db.Boolean, nullable=False)
    stealth = db.Column(db.Boolean, nullable=False)

    arcana = db.Column(db.Boolean, nullable=False)
    history = db.Column(db.Boolean, nullable=False)
    investigation = db.Column(db.Boolean, nullable=False)
    nature = db.Column(db.Boolean, nullable=False)
    religion = db.Column(db.Boolean, nullable=False)

    animal = db.Column(db.Boolean, nullable=False)
    insight = db.Column(db.Boolean, nullable=False)
    medicine = db.Column(db.Boolean, nullable=False)
    perception = db.Column(db.Boolean, nullable=False)
    survival = db.Column(db.Boolean, nullable=False)

    deception = db.Column(db.Boolean, nullable=False)
    intimidation = db.Column(db.Boolean, nullable=False)
    performance = db.Column(db.Boolean, nullable=False)
    persuasion = db.Column(db.Boolean, nullable=False)

    abilities = db.relationship(
        "Ability", secondary="Creature_Ability", backref='ability')

    def __init__(self, name, hp, formula, ac, speed, swimspeed, flyspeed, strength, dex, con, intelligence, wis, cha, strsav, dexsav, consav, intsav, wissav, chasav, cr, proficiency,
                 athletics, acrobatics, soh, stealth, arcana, history, investigation, nature, religion, animal, insight, medicine, perception, survival, deception, intimidation, performance,
                 persuasion):
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
        self.strsav = strsav
        self.dexsav = dexsav
        self.consav = consav
        self.intsav = intsav
        self.wissav = wissav
        self.chasav = chasav
        self.cr = str(cr)
        self.proficiency = proficiency

        self.athletics = athletics
        self.acrobatics = acrobatics
        self.soh = soh
        self.stealth = stealth
        self.arcana = arcana
        self.history = history
        self.investigation = investigation
        self.nature = nature
        self.religion = religion
        self.animal = animal
        self.insight = insight
        self.medicine = medicine
        self.perception = perception
        self.survival = survival
        self.deception = deception
        self.intimidation = intimidation
        self.performance = performance
        self.persuasion = persuasion

    def getProficiencies(self):
        skills = {}
        proficiencies = {}
        skills["Athletics"] = self.athletics
        skills["Acrobatics"] = self.acrobatics
        skills["Sleight of Hand"] = self.soh
        skills["Stealth"] = self.stealth
        skills["Arcana"] = self.arcana
        skills["History"] = self.history
        skills["Investigation"] = self.investigation
        skills["Nature"] = self.nature
        skills["Religion"] = self.religion
        skills["Animal Handling"] = self.animal
        skills["Insight"] = self.insight
        skills["Medicine"] = self.medicine
        skills["Perception"] = self.perception
        skills["Survival"] = self.survival
        skills["Deception"] = self.deception
        skills["Intimidation"] = self.intimidation
        skills["Performance"] = self.performance
        skills["Persuasion"] = self.persuasion

        for skill, prof in skills.items():
            if prof == True:
                proficiencies[skill] = Modifier(self, skill) + self.proficiency
        return proficiencies

    def getSavingThrows(self):
        saves = {}
        saveproficiencies = {}

        saves["STR"] = self.strsav
        saves["DEX"] = self.dexsav
        saves["CON"] = self.consav
        saves["INT"] = self.intsav
        saves["WIS"] = self.wissav
        saves["CHA"] = self.chasav

        for save, prof in saves.items():
            if prof == True:
                saveproficiencies[save] = Modifier(
                    self, save) + self.proficiency
        return saveproficiencies

    @staticmethod
    def find_creatures_with_damage_type(damagetype=''):
        stmt = text("SELECT * FROM CREATURE "
                    "LEFT JOIN Creature_Ability ON Creature.id = Creature_Ability.creature_id "
                    "LEFT JOIN Ability ON Ability.id = Creature_Ability.ability_id "
                    "LEFT JOIN Attack ON Attack.ability_id = Ability.id "
                    "LEFT JOIN Damage_Type ON Damage_Type.id = Attack.DamageType_id "
                    "WHERE DamageType_id = :damagetype").params(damagetype=damagetype)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1], "ac": row[4], "hp": row[2], "formula": row[3], "cr": row[8],
                             "str": row[9], "dex": row[10], "con": row[11], "int": row[12], "wis": row[13], "cha": row[14]})

        return response
