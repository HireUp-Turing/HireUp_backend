import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_

from api import db
from api.database.models import Applicant, Skill, Value

# HELPER METHODS
def _applicant_payload(applicant):

    return {
        'id': applicant.id,
        'username': applicant.username,
        'email': applicant.email,
        'bio': applicant.bio,
        'skills': [skill.name for skill in applicant.skills],
        'values': [value.name for value in applicant.values],
    }

def _filter_applicants(skill_ids, value_ids):
    if skill_ids and value_ids:
        applicants = db.session.query(Applicant).join(Skill, Applicant.skills).join(Value, Applicant.values).filter(or_(Skill.id.in_(skill_ids), Value.id.in_(value_ids)))
    elif skill_ids and not value_ids:
        applicants = db.session.query(Applicant).join(Skill, Applicant.skills).filter(Skill.id.in_(skill_ids))
    elif value_ids and not skill_ids:
        applicants = db.session.query(Applicant).join(Value, Applicant.values).filter(Value.id.in_(value_ids))
    return applicants

class SearchResultsResource(Resource):
    """
    this Resource file is for our /applicants/search endpoint
    """

    def get(self, **kwargs):
        skill_ids = request.json['skills']
        value_ids = request.json['values']

        if not skill_ids and not value_ids:
            return {
                'success': False,
                'error': 400,
                'errors': "At least one skill or value id must be specified in order to filter applicant search results."
            }, 400
        ### will come back to building out this error condition later
        # elif skill_ids is None or value_ids is None:
        #     return {
        #         'success': False,
        #         'error': 400,
        #         'errors': "skill_ids and value_ids keys must be present in request body."
        #     }, 400
        else:
            filtered_applicants = _filter_applicants(skill_ids, value_ids)
            search_results = [_applicant_payload(applicant) for applicant in filtered_applicants]
            return {
                'success': True,
                'data': search_results
            }, 200
