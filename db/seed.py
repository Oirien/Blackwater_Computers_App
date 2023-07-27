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
    user1 = User("Seb", "Morales", "S.Morales@gmail.com")
    user2 = User("Steve", "Mindo", "S.Mindo999@gmail.com")
    user3 = User("Simon", "Malkin", "S.Malkin64@gmail.com")
    component1 = Component("Motherboard", "This is a Motherboard", "This is a picture of a motherboard", 1)
    component2 = Component("CPU", "This is a CPU", "This is a picture of a CPU", 2)
    component3 = Component("GPU", "This is a GPU", "This is a picture of a GPU", 1)
    component4 = Component("Case", "This is a Case", "This is a picture of a Case", 1)
    componentlist1 = ComponentList(1, 1)
    componentlist2 = ComponentList(1, 2)
    componentlist3 = ComponentList(1, 3)
    componentlist4 = ComponentList(1, 4)
    build1 = Build(1,1)