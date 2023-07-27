from app import db

class ComponentList(db.Model):
    __tablename__ = "componentlists"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, db.ForeignKey('components.id'))
    build_id = db.Column(db.Integer, db.ForeignKey('builds.id'))
