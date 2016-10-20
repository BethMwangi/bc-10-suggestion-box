from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask_login import LoginManager
from flask.ext.pagedown import PageDown


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)
pagedown = PageDown(app)
login_manager = LoginManager(app)
login_manager.login_view = 'index'

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app import views, models
