from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime
import uuid

from werkzeug.security import generate_password_hash



login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db = SQLAlchemy()

class Marvel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(100), nullable=False, unique=True)
    super_power = db.Column(db.String(100))
    comics_appeared_in = db.Column(db.String(300))
    hero_or_villain = db.Column(db.String(100))
    description = db.Column(db.String(400))

    def to_dict(self):
        return {
            'id': self.id,
            'Character Name': self.character_name,
            'Superpower': self.super_power,
            'Comics': self.comics_appeared_in,
            'Hero or Villain': self.hero_or_villain,
            'Description': self.description
        }

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), default='')
    last_name = db.Column(db.String(150), default='')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.password = generate_password_hash(password)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid.uuid4())

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'date_created': self.date_created
        }