from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.builds import Build
from app import db

builds_blueprint = Blueprint("builds", __name__)