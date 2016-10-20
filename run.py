from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import manager




 
if __name__ == '__main__':
	manager.run()
