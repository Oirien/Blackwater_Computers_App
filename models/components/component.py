from app import db

class Component(db.Model):
    __tablename__ = "components"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    description = db.Column(db.String())
    image_link = db.Column(db.String(128))
    type = db.Column(db.Integer)


