import datetime
import json

from flask import request
from flask_restful import Resource, abort
# from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant

def _applicant_payload(applicant):
    # figure out syntax for iterating over skills/values (after seeding)
    # skill_names = [skill.name for skill in applicant.skills]
    return {
        'id': applicant.id,
        'username': '',
        'email': applicant.email,
        'skills': 'list_of_skills',
        'values': 'list_of_values'
    }

class ApplicantsResource(Resource):
    """
    this Resource file is for our /users endpoints which don't require
    a resource ID in the URI path
    """

    def get(self, *args, **kwargs):
        applicants = Applicant.query.all()
        results = [_applicant_payload(applicant) for applicant in applicants]
        return {
            'success': True,
            'data': results
        }, 200
