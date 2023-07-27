from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    builds = db.relationship('Build', backref='user')