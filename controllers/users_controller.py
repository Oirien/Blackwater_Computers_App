from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.users import User
from models.builds import Build
from models.components.component import Component
from models.componentlist import ComponentList
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

@users_blueprint.route("/users/new")
def new_user():

    return render_template("users/new.jinja")

@users_blueprint.route("/users", methods=["POST"])
def add_user():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    user = User(first_name=first_name, last_name=last_name, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect('/users')
