from app import db

from models.components.component import *
# from models.components.case import *
# from models.components.cpu_cooler import *
# from models.components.cpu import *
# from models.components.gpu import *
# from models.components.motherboard import *
# from models.components.psu import *
# from models.components.ram import *
# from models.components.storage import *
from models.users import User
from models.builds import Build
from models.componentlist import ComponentList
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    User.query.delete()
    Build.query.delete()
    Component.query.delete()
    ComponentList.query.delete()

    user1 = User(first_name="Seb", last_name="Morales", email="S.Morales@gmail.com")
    user2 = User(first_name="Steve", last_name="Mindo", email="S.Mindo999@gmail.com")
    user3 = User(first_name="Simon", last_name="Malkin", email="S.Malkin64@gmail.com")
    db.session.add_all([user1, user2, user3])
    db.session.commit()

    motherboard1 = Motherboard(name="ASUS Prime Z590-A", description="This is a motherboard description", image_link="This is a motherboard picture", type="Motherboard", price=200, manufacturer="ASUS", power_draw=20, chipset="Z590")
    motherboard2 = Motherboard(name="GIGABYTE B550 AORUS Elite", description="This is a motherboard description", image_link="This is a motherboard picture", type="Motherboard", price=150, manufacturer="GIGABYTE", power_draw=25, chipset="B550")
    motherboard3 = Motherboard(name="MSI B450 TOMAHAWK MAX", description="This is a motherboard description", image_link="This is a motherboard picture", type="Motherboard", price=120, manufacturer="MSI", power_draw=18, chipset="B450")
    db.session.add_all([motherboard1, motherboard2, motherboard3])
    db.session.commit()

    cpu1 = Cpu(name="Intel Core i9-13900K", description="This is a CPU description", image_link="This is a cpu picture", type="CPU", price=500, manufacturer="Intel", power_draw=150, chipset="LGA 1200")
    cpu2 = Cpu(name="AMD Ryzen 9 5950X", description="This is a CPU description", image_link="This is a cpu picture", type="CPU", price=400, manufacturer="AMD", power_draw=120, chipset="AM4")
    cpu3 = Cpu(name="Intel Core i5-12600K", description="This is a CPU description", image_link="This is a cpu picture", type="CPU", price=300, manufacturer="Intel", power_draw=100, chipset="LGA 1200")
    db.session.add_all([cpu1, cpu2, cpu3])
    db.session.commit()