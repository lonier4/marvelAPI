from flask import Flask
from config import Config

# blueprint imports
from .characters.routes import characters
from .authorization.routes import auth
from .api.routes import api

# database imports
from .models import db, login
from flask_migrate import Migrate

app = Flask(__name__)

# blueprint registrations
app.register_blueprint(characters)
app.register_blueprint(auth)
app.register_blueprint(api)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.signin'
login.login_message = 'Please log in to see this page'
login.login_message_category = 'alert-info'

from . import routes
from . import models