from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.users import User
from app import db

users_blueprint = Blueprint("users", __name__)