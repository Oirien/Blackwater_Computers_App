from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.components.component import Component
from app import db

components_blueprint = Blueprint("components", __name__)