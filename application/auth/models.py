from application._init_ import db


class AccountRole(db.Model):
   __tablename__ = "account_role"
   id = db.Column(db.Integer, primary_key=True)
   role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
   user_id = db.Column(db.Integer, db.ForeignKey('account.id'))

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    roles = db.relationship("Role", secondary="account_role", backref='role', lazy=True)

    def __init__(self, name, username, password, roles):
        self.name = name
        self.username = username
        self.password = password
        self.roles = roles
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(40), nullable=False)
    accounts = db.relationship("User", secondary="account_role")