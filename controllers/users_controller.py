from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.users import User
from models.builds import Build
from models.components.component import Component
from app import db

users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = User.query.all()
    return render_template("users/index.jinja", users=users)

@users_blueprint.route("/users/<id>")
def single_user(id):
    user = User.query.get(id)
    builds = Build.query.all()
    components = Component.query.all()
    return render_template("users/show.jinja", user=user, builds=builds, components=components)