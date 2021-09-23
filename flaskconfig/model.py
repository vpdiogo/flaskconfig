from flask_sqlalchemy import SQLAlchemy
from config import app_config, app_active

config = app_config[app_active]
db = SQLAlchemy(config.app)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True) 
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)