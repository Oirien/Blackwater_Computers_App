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
    ComponentList.query.delete()
    Build.query.delete()
    Component.query.delete()      
    
    user1 = User(first_name="Seb", last_name="Morales", email="S.Morales@gmail.com")
    user2 = User(first_name="Steve", last_name="Mindo", email="S.Mindo999@gmail.com")
    user3 = User(first_name="Simon", last_name="Malkin", email="S.Malkin64@gmail.com")
    db.session.add_all([user1, user2, user3])
    db.session.commit()

    case1 = Case(name="NZXT H510", description="This is a case description", image_link="This is a case picture", price=80, manufacturer="NZXT")
    case2 = Case(name="Corsair iCUE 4000X RGB", description="This is a case description", image_link="This is a case picture", price=100, manufacturer="Corsair")
    case3 = Case(name="Lian Li O11 DYNAMIC", description="This is a case description", image_link="This is a case picture", price=90, manufacturer="Lian Li")
    db.session.add_all([case1, case2, case3])
    db.session.commit()

    psu1 = Psu(name="EVGA SuperNOVA 850 G5", description="This is a PSU description", image_link="This is a psu picture", price=150, manufacturer="EVGA", power_supply=850)
    psu2 = Psu(name="Corsair RM750x", description="This is a PSU description", image_link="This is a psu picture", price=120, manufacturer="Corsair", power_supply=750)
    psu3 = Psu(name="Seasonic Focus GX-650", description="This is a PSU description", image_link="This is a psu picture", price=100, manufacturer="Seasonic", power_supply=650)
    db.session.add_all([psu1, psu2, psu3])
    db.session.commit()

    motherboard1 = Motherboard(name="ASUS Prime Z590-A", description="This is a motherboard description", image_link="This is a motherboard picture", price=200, manufacturer="ASUS", power_draw=20, chipset="LGA1200")
    motherboard2 = Motherboard(name="GIGABYTE B550 AORUS Elite", description="This is a motherboard description", image_link="This is a motherboard picture", price=150, manufacturer="GIGABYTE", power_draw=25, chipset="AM4")
    motherboard3 = Motherboard(name="MSI B450 TOMAHAWK MAX", description="This is a motherboard description", image_link="This is a motherboard picture", price=120, manufacturer="MSI", power_draw=18, chipset="AM4")
    db.session.add_all([motherboard1, motherboard2, motherboard3])
    db.session.commit()

    cpu1 = Cpu(name="Intel Core i9-13900K", description="This is a CPU description", image_link="This is a cpu picture", price=500, manufacturer="Intel", power_draw=150, chipset="LGA 1200")
    cpu2 = Cpu(name="AMD Ryzen 9 5950X", description="This is a CPU description", image_link="This is a cpu picture", price=400, manufacturer="AMD", power_draw=120, chipset="AM4")
    cpu3 = Cpu(name="Intel Core i5-12600K", description="This is a CPU description", image_link="This is a cpu picture", price=300, manufacturer="Intel", power_draw=100, chipset="LGA 1200")
    db.session.add_all([cpu1, cpu2, cpu3])
    db.session.commit()

    cooler1 = Cpu_Cooler(name="Noctua NH-D15", description="This is a CPU Cooler description", image_link="This is a cooler picture", price=100, manufacturer="Noctua")
    cooler2 = Cpu_Cooler(name="be quiet! Dark Rock Pro 4", description="This is a CPU Cooler description", image_link="This is a cooler picture", price=90, manufacturer="be quiet!")
    cooler3 = Cpu_Cooler(name="Cooler Master Hyper 212 EVO", description="This is a CPU Cooler description", image_link="This is a cooler picture", price=40, manufacturer="Cooler Master")
    db.session.add_all([cooler1, cooler2, cooler3])
    db.session.commit()

    gpu1 = Gpu(name="NVIDIA GeForce RTX 4080ti", description="This is a GPU description", image_link="This is a gpu picture", price=800, manufacturer="NVIDIA", power_draw=400)
    gpu2 = Gpu(name="AMD Radeon RX 7900 XTX", description="This is a GPU description", image_link="This is a gpu picture", price=700, manufacturer="AMD", power_draw=355)
    gpu3 = Gpu(name="Intel Arc A770", description="This is a GPU description", image_link="This is a gpu picture", price=600, manufacturer="Intel", power_draw=225)
    db.session.add_all([gpu1, gpu2, gpu3])
    db.session.commit()

    ram1 = Ram(name="Corsair Vengeance LPX 16GB", description="This is a RAM description", image_link="This is a ram picture", price=80, manufacturer="Corsair", power_draw=5)
    ram2 = Ram(name="G.SKILL Ripjaws V Series 32GB", description="This is a RAM description", image_link="This is a ram picture", price=120, manufacturer="G.SKILL", power_draw=8)
    ram3 = Ram(name="Crucial Ballistix 16GB", description="This is a RAM description", image_link="This is a ram picture", price=70, manufacturer="Crucial", power_draw=6)
    db.session.add_all([ram1, ram2, ram3])
    db.session.commit()

    storage1 = Storage(name="Samsung 970 EVO 1TB", description="This is a storage description", image_link="This is a ssd picture", price=200, manufacturer="Samsung", power_draw=7)
    storage2 = Storage(name="WD Blue 2TB", description="This is a storage description", image_link="This is a ssd picture", price=150, manufacturer="WD", power_draw=6)
    storage3 = Storage(name="Seagate BarraCuda 4TB", description="This is a storage description", image_link="This is a hdd picture", price=180, manufacturer="Seagate", power_draw=8)
    db.session.add_all([storage1, storage2, storage3])
    db.session.commit()

    build1 = Build(user_id=1)
    build2 = Build(user_id=2)
    build3 = Build(user_id=3)
    db.session.add_all([build1, build2, build3])
    db.session.commit()

    componentlist1 = ComponentList(build_id=1, component_id=1)
    componentlist2 = ComponentList(build_id=1, component_id=4)
    componentlist3 = ComponentList(build_id=1, component_id=7)
    componentlist4 = ComponentList(build_id=1, component_id=10)
    componentlist5 = ComponentList(build_id=1, component_id=13)
    componentlist6 = ComponentList(build_id=1, component_id=16)
    componentlist7 = ComponentList(build_id=1, component_id=19)
    componentlist8 = ComponentList(build_id=1, component_id=22)
    db.session.add_all([componentlist1, componentlist2, componentlist3, componentlist4, componentlist5, componentlist6, componentlist7, componentlist8])
    db.session.commit()

    componentlist10 = ComponentList(build_id=2, component_id=2)
    componentlist11 = ComponentList(build_id=2, component_id=5)
    componentlist12 = ComponentList(build_id=2, component_id=8)
    componentlist13 = ComponentList(build_id=2, component_id=11)
    componentlist14 = ComponentList(build_id=2, component_id=14)
    componentlist15 = ComponentList(build_id=2, component_id=17)
    componentlist16 = ComponentList(build_id=2, component_id=20)
    componentlist17 = ComponentList(build_id=2, component_id=23)
    db.session.add_all([componentlist10, componentlist11, componentlist12, componentlist13, componentlist14, componentlist15, componentlist16, componentlist17])
    db.session.commit()

    componentlist19 = ComponentList(build_id=3, component_id=3)
    componentlist20 = ComponentList(build_id=3, component_id=6)
    componentlist21 = ComponentList(build_id=3, component_id=9)
    componentlist22 = ComponentList(build_id=3, component_id=12)
    componentlist23 = ComponentList(build_id=3, component_id=15)
    componentlist24 = ComponentList(build_id=3, component_id=18)
    componentlist25 = ComponentList(build_id=3, component_id=21)
    componentlist26 = ComponentList(build_id=3, component_id=24)
    db.session.add_all([componentlist19, componentlist20, componentlist21, componentlist22, componentlist23, componentlist24, componentlist25, componentlist26])
    db.session.commit()