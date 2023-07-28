from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.builds import Build
from models.components.component import Component
from models.users import User
from models.componentlist import ComponentList
from app import db

builds_blueprint = Blueprint("builds", __name__)

@builds_blueprint.route("/builds")
def builds():
    builds = Build.query.all()
    users = User.query.all()
    return render_template("builds/index.jinja", builds=builds, users=users)

@builds_blueprint.route("/builds/<id>")
def single_build(id):
    build = Build.query.get(id)
    users = User.query.all()
    components = Component.query.all()
    return render_template("builds/show.jinja", build=build, users=users, components=components)

@builds_blueprint.route("/builds/new")
def build_form():
     users = User.query.all()
     components = Component.query.all()
     component_types = list(set(component.type for component in components))

     return render_template('builds/new.jinja', users=users, components=components, component_types=component_types)

@builds_blueprint.route("/builds", methods=['POST'])
def new_build():
    user_id = request.form.get('user')
    component_ids = []

    for component_type in request.form:
        if component_type != 'user' and request.form[component_type] != '':
            component_id = int(request.form[component_type])
            component_ids.append(component_id)

    build = Build(user_id=user_id)
    db.session.add(build)
    db.session.commit()

    for component_id in component_ids:
        component_list = ComponentList(component_id=component_id, build_id=build.id)
        db.session.add(component_list)

    db.session.commit()

    return redirect("/builds")