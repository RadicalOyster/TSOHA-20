from application._init_ import db

class Creature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    formula = db.Column(db.String)
    ac = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer)
    swimspeed = db.Column(db.Integer)
    flyspeed = db.Column(db.Integer)
    cr = db.Column(db.String)
    str = db.Column(db.Integer, nullable=False)
    dex = db.Column(db.Integer, nullable=False)
    con = db.Column(db.Integer, nullable=False)
    int = db.Column(db.Integer, nullable=False)
    wis = db.Column(db.Integer, nullable=False)
    cha = db.Column(db.Integer, nullable=False)

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