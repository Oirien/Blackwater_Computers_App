from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.components.component import Component
from app import db

components_blueprint = Blueprint("components", __name__)

@components_blueprint.route("/components")
def components():
    component_types = Component.query.with_entities(Component.type).distinct().all()
    return render_template("components/index.jinja", component_types=component_types)


@components_blueprint.route("/components/sort/<type>")
def component_type(type):
    components = Component.query.filter_by(type=type).all()
    return render_template("components/sort.jinja", components=components, type=type)

@components_blueprint.route("/components/show/<id>")
def component_show(id):
    component = Component.query.get(id)
    return render_template("components/show.jinja", component=component)