from app import db

from models.components.component import *
from models.components.case import *
from models.components.cpu_cooler import *
from models.components.cpu import *
from models.components.gpu import *
from models.components.motherboard import *
from models.components.psu import *
from models.components.ram import *
from models.components.storage import *
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
    component1 = Component(name="Motherboard", description="This is a Motherboard", image_link="This is a picture of a motherboard", type=1)
    component2 = Component(name="CPU", description="This is a CPU", image_link="This is a picture of a CPU", type=2)
    component3 = Component(name="GPU", description="This is a GPU", image_link="This is a picture of a GPU", type=3)
    component4 = Component(name="Case", description="This is a Case", image_link="This is a picture of a Case", type=4)
    componentlist1 = ComponentList(build_id=1, component_id=1)
    componentlist2 = ComponentList(build_id=1, component_id=2)
    componentlist3 = ComponentList(build_id=1, component_id=3)
    componentlist4 = ComponentList(build_id=1, component_id=4)
    build1 = Build(user_id=1)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(component1)
    db.session.add(component2)
    db.session.add(component3)
    db.session.add(component4)
    db.session.add(componentlist1)
    db.session.add(componentlist2)
    db.session.add(componentlist3)
    db.session.add(componentlist4)
    db.session.add(build1)

    db.session.commit()