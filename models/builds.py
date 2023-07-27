from app import db

class Build(db.Model):
    __tablename__ = "builds"

    id = db.Column(db.Integer, primary_key=True)
    componentlist = db.relationship('componentlists', backref='builds')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))