# File to configure Manager from flask-script, which is like Rake tasks for Flask
from flask_script import Manager
# include the next line when dealing with migrations
from flask_migrate import Migrate, MigrateCommand

from api import create_app, db
from api.database.models import Applicant

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

# manage migrations
manager.add_command('db', MigrateCommand)

@manager.command
# equivalent to 'rake routes' in Rails
def routes():
    print(app.url_map)

# Seeding of DB!
@manager.command
def db_seed():
    db.drop_all()
    db.create_all()

    # Seeds
    # Look up how to make a seeds file and then
    # call it here.
    applicant = Applicant(email='gaby@hireup.com', first_name='Gaby', last_name='Mendez')
    db.session.add(applicant)

    db.session.commit()
    print(f'obj count: {len(db.session.query(Applicant).all())}')

if __name__ == "__main__":
    manager.run()
