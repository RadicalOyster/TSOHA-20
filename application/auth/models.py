from application._init_ import db
from sqlalchemy.sql import text


class AccountRole(db.Model):
    __tablename__ = "account_role"
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'))


class AccountCreature(db.Model):
    _tablename_ = "account_creature"
    id = db.Column(db.Integer, primary_key=True)
    creature_id = db.Column(db.Integer, db.ForeignKey('creature.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('account.id'))


class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    roles = db.relationship("Role", secondary="account_role", backref='role', lazy=True)
    creatures = db.relationship("Creature", secondary="account_creature", backref='creature', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.roles = []
        self.creatures = []

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def initialize_admin():
        try:
            stmt = text(
                "INSERT INTO Account (name, username, password) VALUES ('Admin', 'Admin', 'Admin')")
            db.engine.execute(stmt)
            stmt = text(
                "INSERT INTO Account_Role (user_id, role_id) VALUES (1, 1)")
            db.engine.execute(stmt)
            stmt = text(
                "INSERT INTO Account_Role (user_id, role_id) VALUES (1, 2)")
            db.engine.execute(stmt)
        except:
            pass


class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(40), nullable=False, unique=True)
    accounts = db.relationship("User", secondary="account_role")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def initialize_roles():
        try:
            stmt = text("INSERT INTO Role (name) VALUES ('ADMIN')")
            db.engine.execute(stmt)
            stmt = text("INSERT INTO Role (name) VALUES ('USER')")
            db.engine.execute(stmt)
        except:
            pass

    @staticmethod
    def find_role_by_name(name):
        stmt = text("SELECT role.id, role.name FROM role"
                    " WHERE role.name = :name").params(name=name)
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response
