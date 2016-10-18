import os


basedir = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-never-know'


# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')