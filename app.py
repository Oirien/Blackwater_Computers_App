from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://Rob:123@localhost:5432/blackwater_computers"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from db.seed import seed
app.cli.add_command(seed)

from controllers.builds_controller import  builds_blueprint
from controllers.components_controller import  components_blueprint
from controllers.users_controller import  users_blueprint

app.register_blueprint(builds_blueprint)
app.register_blueprint(components_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/home')
def home():
    return render_template('index.jinja')

@app.route('/')
def home_redirect():
    return redirect('/home')