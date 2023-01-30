from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)
    
    # favs = db.relationship('Favs', backref='user', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active,
            "username":self.username,
         # do not serialize the password, its a security breach
        }


# ________________favs______________________

# class Favs(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
#     characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
#     planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=True)
#     vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=True)

#     def __repr__(self):
#         return '<Favs %r>' % self.id

#     def serialize(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "characters_id": self.characters_id,
#             "planets_id": self.planets_id,
#             "vehicles_id": self.vehicles_id,
#             # do not serialize the password, its a security breach
#         }

#_________________characters__________________________

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    hairColor = db.Column(db.String(250), nullable=True)
    gender = db.Column(db.String(250), nullable=True)
    # favs = db.relationship('Favs', backref='characters', lazy=True)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            # do not serialize the password, its a security breach
        }
#___________________planets________________________

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    # favs = db.relationship('Favs', backref='planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            # do not serialize the password, its a security breach
        }

#_______________vehicles________________________________

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    # favs = db.relationship('Favs', backref='vehicles', lazy=True)

    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }


