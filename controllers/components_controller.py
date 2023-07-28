from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.components.component import Component
from app import db

components_blueprint = Blueprint("components", __name__)

@components_blueprint.route("/components")
def components():
    components = Component.query.all()
    return render_template("components/index.jinja", components=components)

@components_blueprint.route("/components/<type>")
def component_type(type):
    component_type = Component.query.filter_by(type = type)
    return render_template("components/sort.jinja", components=component_type)