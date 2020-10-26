# File to configure Manager from flask-script, which is like Rake tasks for Flask
from flask_script import Manager
# include the next line when dealing with migrations
# from flask_migrate import Migrate, MigrateCommand

from api import create_app, db
# doesn't exist yet
# from api.database.models import User

app = create_app()
# migrate = Migrate(app, db)
manager = Manager(app)

@manager.command
# equivalent to 'rake routes' in Rails
def routes():
    print(app.url_map)

# write more commands here to enable db migration & seeding

if __name__ == "__main__":
    manager.run()
