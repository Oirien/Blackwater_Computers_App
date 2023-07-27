from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://Rob:123@localhost:5432/blackwater_computers"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from db.seed import seed
app.cli.add_command(seed)
