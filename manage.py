# File to configure Manager from flask-script, which is like Rake tasks for Flask
from flask_script import Manager
# include the next line when dealing with migrations
from flask_migrate import Migrate, MigrateCommand

from api import create_app, db
from api.database.models import Applicant, Value

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

# manage migrations
manager.add_command('db', MigrateCommand)

@manager.command
# equivalent to 'rake routes' in Rails
def routes():
    print(app.url_map)

# write more commands here to enable db migration & seeding
@manager.command
def db_seed():
    db.drop_all()
    db.create_all()

    # seed anything here we might need
    gaby = Applicant(email='gaby@hireup.com', first_name='Gaby', last_name='Mendez')
    db.session.add(gaby)

    ruthie = Applicant(email='ruthie@hireup.com', first_name='Ruthie', last_name='Rabinovitch')
    db.session.add(ruthie)

    creativity = Value(name='creativity')
    db.session.add(creativity)

    db.session.commit()
    # this is just a return value for confirmation.
    # counts objects seeded
    print(f'obj count: {len(db.session.query(Applicant).all())}')

if __name__ == "__main__":
    manager.run()
