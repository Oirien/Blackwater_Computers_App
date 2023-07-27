from app import db

class Build(db.Model):
    __tablename__ = "build"

    id = db.Column(db.Integer, primary_key=True)
    componentlist_id = db.Column(db.Integer, db.ForeignKey('componentlist.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))