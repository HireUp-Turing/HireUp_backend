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

    java = Skill(name='java')
    db.session.add(java)

    js = Skill(name='javascript')
    db.session.add(js)
    
    react = Skill(name='react')
    db.session.add(react)
    
    ts = Skill(name='typescript')
    db.session.add(ts)

    redux = Skill(name='redux')
    db.session.add(redux)
    
    git = Skill(name='git')
    db.session.add(git)

    microsoft = Skill(name='microsoft')
    db.session.add(microsoft)
    
    adobe = Skill(name='Adobe Creative Suites')
    db.session.add(adobe)
    
    vue = Skill(name='vue')
    db.session.add(vue)
    
    angular = Skill(name='angular')
    db.session.add(angular)
    
    express = Skill(name='express')
    db.session.add(express)
    
    knex = Skill(name='knex')
    db.session.add(knex)
    
    psql = Skill(name='Postgres')
    db.session.add(psql)
    
    communication = Skill(name='communication')
    db.session.add(communication)

    critical_thinking = Skill(name'critical thinking')
    db.session.add(critical_thinking)

    problem_solving = Skill(name'problem solving')
    db.session.add(problem_solving)

    public_speaking = Skill(name'public speaking')
    db.session.add(public_speaking)

    customer_service = Skill(name'customer service')
    db.session.add(customer_service)

    teamwork = Skill(name'teamwork')
    db.session.add(teamwork)"

    active_listening = Skill(name'active listening')    
    db.session.add(active_listening)
    
    negotiation = Skill(name'negotiation')
    db.session.add(negotiation)

    conflict_resolution = Skill(name'conflict resolution')
    db.session.add(conflict_resolution)
    
    empathy = Skill(name'empathy')
    db.session.add(empathy)

    decision_making = Skill(name'decision making')
    db.session.add(decision_making)

    management = Skill(name'management')
    db.session.add(management)

    leadership = Skill(name'leadership')
    db.session.add(leadership)

    organization = Skill(name'organization')
    db.session.add(organization)

    foreign_languages = Skill(name'foreign languages')
    db.session.add(foreign_languages)

    social_media = Skill(name'social media')
    db.session.add(social_media)

    teaching = Skill(name'teaching')
    db.session.add(teaching)
    
    design = Skill(name'design')
    db.session.add(design)

    project_management = Skill(name'project management')
    db.session.add(project_management)

    computer_technology = Skill(name'computer technology')
    db.session.add(computer_technology)

    accounting = Skill(name'accounting')
    db.session.add(accounting)

    business_data = Skill(name'business & data analysis')
    db.session.add(business_data)

    nursing = Skill(name'nursing')
    db.session.add(nursing)

    economics = Skill(name'economics')
    db.session.add(economics)

    automotive_services = Skill(name'automotive services')
    db.session.add(automotive_servcices)

    seo = Skill(name'SEO/SEM marketing)
    db.session.add(seo)
    
    cloud = Skill(name'cloud and distributed')
    db.session.add(cloud)
        
    data_pres = Skill(name'data presentation')
    db.session.add(data_pres)

    engage = Value(name'engages with community')
    db.session.add(engage)

    diverse = Value(name'team is diverse')
    db.session.add(diverse)

    feedback = Value(name'continuous feedback')
    db.session.add(feedback)

    impressive = Value(name'impressive team members')
    db.session.add(impressive)

    bond = Value(name'bonded by love for product')
    db.session.add(bond)

    innovative = Value(name'creative & innovative')
    db.session.add(innovative)

    collaboration = Value(name'cross-department collaboration')
    db.session.add(collaboration)

    open_coms = Value(name'open communication')
    db.session.add(open_coms)

    eq_iq = Value(name'eq > iq')
    db.session.add(eq_iq)

    flat_org = Value(name'flat organizations')
    db.session.add(flat_org)

    risk_taking = Value(name'risk taking > stability')
    db.session.add(risk_taking)

    hats = Value(name'wears many hats')
    db.session.add(hats)
                
    heavy_team = Value(name'heavily team oriented')
    db.session.add(heavy_team)

    promotes = Value(name'promotes from within')
    db.session.add(promotes)

    mobility = Value(name'internal mobility')
    db.session.add(mobility)

    juniors = Value(name'good for juniors')
    db.session.add(juniors)

    interns = Value(name'has internships')
    db.session.add(interns)

    retention = Value(name'high employee retention')
    db.session.add(retention)

    inclusion = Value(name'actively practices inclusion')
    db.session.add(inclusion)

    work_life = Value(name'work life balance')
    db.session.add(work_life)

    personal_growth = Value(name'committed to personal growth')
    db.session.add(personal_growth)

    parents = Value(name'ideal for parents')
    db.session.add(parents)

    safe_fail = Value(name'safe environment to fail')
    db.session.add(safe_fail)

    physical_wellness = Value(name'supports physical wellness')
    db.session.add(physical_wellness)
    
    psychological = Value(name'supports mental health') 
    db.session.add(psychological)

    lunch = Value(name'eats lunch together')
    db.session.add(lunch)

    flexx = Value(name'flexible work arrangements')
    db.session.add(flexx)

    light_mtgs = Value(name'light meetings')
    db.session.add(light_mtgs)

    friends = Value(name'friends outside of work')
    db.session.add(friends)
    
    beer = Value(name'has good beer')
    db.sessions.add(beer)

    layout = Value(name'thoughtful office layout')
    db.sessions.add(layout)

    customer = Value(name'customer first')
    db.sessions.add(customer)

    engineer = Value(name'engineering-driven')  
    db.sessions.add(engineer)
                
    product = Value(name'product-driven')
    db.sessions.add(product)
    
    design_driven = Value(name'design-driven')
    db.sessions.add(design_driven)

    data_driven = Values(name'data_driven')
    db.sessions.add(data_driven)

    rapid_growth = Values(name'rapidly growing team')
    db.sessions.add(rapid_growth)

    bb = Values(name'B2B')
    db.sessions.add(bb)

    bc = Values(name'B2C')
    db.sessions.add(bc)

    self_funded = Values(name'self funded')
    db.sessions.add(self_funded)
                
    tech_founders = Values(name'technical founder(s)')
    db.sessions.add(tech_founders)
                
    PBC = Values(name'PBC / B-CORP')
    db.sessions.add(PBC)

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
