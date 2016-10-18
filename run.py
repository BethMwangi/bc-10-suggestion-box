from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import manager



# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

# from app import app
# app.run(debug=True)





# from app.models import User, Post
# from flask.ext.migrate import Migrate, MigrateCommand



 
if __name__ == '__main__':
	manager.run()

