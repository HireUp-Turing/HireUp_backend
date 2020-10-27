import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant

def _applicant_payload(applicant):

    return {
        'id': applicant.id,
        'username': applicant.username,
        'email': applicant.email,
        'bio': applicant.bio,
        # 'skills': [{'id': skill.id, 'name': skill.name} for skill in applicant.skills],
        'skills': [skill.name for skill in applicant.skills],
        'values': [value.name for value in applicant.values]
    }

class ApplicantsResource(Resource):
    """
    this Resource file is for our /applicants endpoints which don't require
    a resource ID in the URI path
    """

    def get(self, *args, **kwargs):
        applicants = Applicant.query.all()
        results = [_applicant_payload(applicant) for applicant in applicants]
        return {
            'success': True,
            'data': results
        }, 200

class ApplicantResource(Resource):
    """
    this Resource file is for our /applicants/:id endpoints
    GET /applicants/:id
    DELETE, PATCH
    """
    def get(self, *args, **kwargs):
        # kwargs == params
        applicant_id = kwargs['applicant_id']
        applicant = None
        try:
            applicant = db.session.query(Applicant).filter_by(id=applicant_id).one()
        except NoResultFound:
            return abort(404)

        return {
            'success': True,
            'data': _applicant_payload(applicant)
        }, 200
