from app import db

class ComponentList(db.Model):
    __tablename__ = "componentlist"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, db.ForeignKey('component.id'))
    build_id = db.Column(db.Integer, db.ForeignKey('build.id'))