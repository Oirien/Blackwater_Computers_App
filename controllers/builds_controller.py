from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.builds import Build
from models.components.component import Component
from models.users import User
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