from app import db
from sqlalchemy.ext.declarative import declared_attr

class Component(db.Model):
    __tablename__ = "components"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    description = db.Column(db.String())
    image_link = db.Column(db.String(128))
    type = db.Column(db.String(64))
    price = db.Column(db.Integer)
    manufacturer = db.Column(db.String(64))

    __mapper_args__ = {
        'polymorphic_identity': 'component',
        'polymorphic_on': type
    }

class Cpu(Component):
    __tablename__ = "cpus"

    power_draw = db.Column(db.Integer)
    chipset = db.Column(db.String(64))
    type = db.Column(db.String(64), default='CPU')

    @declared_attr
    def type(cls):
        return Component.__table__.c.type

    

    __mapper_args__ = {
        'polymorphic_identity': 'CPU'
    }

class Case(Component):
    __tablename__ = "cases"

    type = db.Column(db.String(64), default='Case')

    @declared_attr
    def type(cls):
        return Component.__table__.c.type

    __mapper_args__ = {
        'polymorphic_identity': 'Case'
    }
    
class Cpu_Cooler(Component):
    __tablename__ = "cpu_coolers"

    type = db.Column(db.String(64), default='CPU Cooler')

    @declared_attr
    def type(cls):
        return Component.__table__.c.type

    __mapper_args__ = {
        'polymorphic_identity': 'CPU Cooler'
    }

class Gpu(Component):
    __tablename__ = "gpus"

    power_draw = db.Column(db.Integer)
    type = db.Column(db.String(64), default='GPU')

    @declared_attr
    def type(cls):
        return Component.__table__.c.type
    
    @declared_attr
    def power_draw(cls):
        return Component.__table__.c.power_draw

    __mapper_args__ = {
        'polymorphic_identity': 'GPU'
    }

class Motherboard(Component):
    __tablename__ = "motherboards"

    power_draw = db.Column(db.Integer)
    chipset = db.Column(db.String(64))
    type = db.Column(db.String(64), default='Motherboard')

    @declared_attr
    def type(cls):
        return Component.__table__.c.type

    @declared_attr
    def power_draw(cls):
        return Component.__table__.c.power_draw
    
    @declared_attr
    def chipset(cls):
        return Component.__table__.c.chipset
    
    __mapper_args__ = {
        'polymorphic_identity': 'Motherboard'
    }

class Psu(Component):
    __tablename__ = "psus"

    power_supply = db.Column(db.Integer)
    type = db.Column(db.String(64), default='PSU')

    @declared_attr
    def type(cls):
        return Component.__table__.c.type
    
    __mapper_args__ = {
        'polymorphic_identity': 'PSU'
    }

class Ram(Component):
    __tablename__ = "rams"

    power_draw = db.Column(db.Integer)
    type = db.Column(db.String(64), default='RAM')

    @declared_attr
    def type(cls):
        return Component.__table__.c.type

    @declared_attr
    def power_draw(cls):
        return Component.__table__.c.power_draw
    
    __mapper_args__ = {
        'polymorphic_identity': 'RAM'
    }

class Storage(Component):
    __tablename__ = "storages"

    power_draw = db.Column(db.Integer)
    type = db.Column(db.String(64), default='Storage')

    @declared_attr
    def type(cls):
        return Component.__table__.c.type
    
    @declared_attr
    def power_draw(cls):
        return Component.__table__.c.power_draw
    
    __mapper_args__ = {
        'polymorphic_identity': 'Storage'
    }
