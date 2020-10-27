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

    api.add_resource(ApplicantResource, '/api/v1/applicants/<applicant_id>')
    api.add_resource(ApplicantsResource, '/api/v1/applicants')

    return app
