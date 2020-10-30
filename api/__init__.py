from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
# from werkzeug.exceptions import HTTPException
from config import config

db = SQLAlchemy()

def create_app(config_name='default'):
    # creates a Flask instance
    app = Flask(__name__)
    # __name__ is the name of the current Python module,
    # tells the app where it's located

    app.config.from_object(config[config_name])

    # set up database
    db.init_app(app)

    # set up CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # set up Flask-RESTful
    # this allows methods like api.add_resource to be used later on
    api = Api(app)

    # test route
    @app.route('/')
    def root():
        return 'Hello World!'

    # Add resources
    from api.resources.applicants import ApplicantsResource, ApplicantResource
    from api.resources.messages import MessagesResource, MessageResource
    from api.resources.search_options import SearchOptionsResource
    from api.resources.skills import SkillsResource
    from api.resources.values import ValuesResource

    api.add_resource(ApplicantResource, '/api/v1/applicants/<applicant_id>')
    api.add_resource(ApplicantsResource, '/api/v1/applicants')
    api.add_resource(MessageResource, '/api/v1/messages/<message_id>')
    api.add_resource(MessagesResource, '/api/v1/messages')
    api.add_resource(SearchOptionsResource, '/api/v1/applicants/search-options')
    api.add_resource(SkillsResource, '/api/v1/skills')
    api.add_resource(ValuesResource, '/api/v1/values')

    return app
