# File to configure Manager from flask-script, which is like Rake tasks for Flask
from flask_script import Manager
# include the next line when dealing with migrations
from flask_migrate import Migrate, MigrateCommand

from api import create_app, db
from api.database.models import Applicant, Value, Skill, Message

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
    gaby = Applicant(email='gaby@hireup.com', first_name='Gaby', last_name='Mendez', bio="Noodle's mom!")
    db.session.add(gaby)

    ruthie = Applicant(email='ruthie@hireup.com', first_name='Ruthie', last_name='Rabinovitch', bio='Noodle\'s mom\'s accountabilabuddy!')
    db.session.add(ruthie)

    creativity = Value(name='creativity')
    db.session.add(creativity)

    mentorship = Value(name='mentorship')
    db.session.add(mentorship)

    rails = Skill(name='rails')
    db.session.add(rails)

    flask = Skill(name='flask')
    db.session.add(flask)

    ruby = Skill(name='ruby')
    db.session.add(ruby)

    message1 = Message(employer_name='Turing', employer_email='info@turing.com', body='This is a message from Turing! You are awesome.')
    ruthie.messages.append(message1)

    message2 = Message(employer_name='Basecamp', employer_email='info@basecamp.com', body='Come work for us.')
    ruthie.messages.append(message2)

    ruthie.skills.append(rails)
    ruthie.skills.append(flask)
    ruthie.values.append(creativity)
    ruthie.values.append(mentorship)

    gaby.skills.append(rails)
    gaby.skills.append(ruby)
    gaby.values.append(creativity)

    db.session.commit()
    # this is just a return value for confirmation.
    # counts objects seeded
    print(f'obj count: {len(db.session.query(Applicant).all())}')

if __name__ == "__main__":
    manager.run()
