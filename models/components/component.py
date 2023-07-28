from app import db

class Component(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    description = db.Column(db.String())
    image_link = db.Column(db.String(128))
    type = db.Column(db.String(64))
    price = db.Column(db.Integer)
    manufacturer = db.Column(db.String(64))

class Cpu(Component):
    __tablename__ = "cpus"

    id = db.Column(db.Integer, primary_key = True)
    power_draw = db.Column(db.Integer)
    chipset = db.Column(db.String(64))

class Case(Component):
    __tablename__ = "cases"

    id = db.Column(db.Integer, primary_key = True)
    
class Cpu_Cooler(Component):
    __tablename__ = "cpu_coolers"
    id = db.Column(db.Integer, primary_key = True)

class Gpu(Component):
    __tablename__ = "gpus"

    id = db.Column(db.Integer, primary_key = True)
    power_draw = db.Column(db.Integer)

class Motherboard(Component):
    __tablename__ = "motherboards"

    id = db.Column(db.Integer, primary_key = True)
    power_draw = db.Column(db.Integer)
    chipset = db.Column(db.String(64))

class Psu(Component):
    __tablename__ = "psus"

    id = db.Column(db.Integer, primary_key = True)
    power_supply = db.Column(db.Integer)

class Ram(Component):
    __tablename__ = "rams"

    id = db.Column(db.Integer, primary_key = True)
    power_draw = db.Column(db.Integer)

class Storage(Component):
    __tablename__ = "storages"

    id = db.Column(db.Integer, primary_key = True)
    power_draw = db.Column(db.Integer)
