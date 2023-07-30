from app import db

class Build(db.Model):
    __tablename__ = "builds"

    id = db.Column(db.Integer, primary_key=True)
    componentlist = db.relationship('ComponentList', backref='builds')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    completed = db.Column(db.Boolean, default=False)
    delivered = db.Column(db.Boolean, default=False)