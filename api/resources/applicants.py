
import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant, ApplicantSkill, ApplicantValue

# HELPER METHODS
def _applicant_payload(applicant):

    return {
        'id': applicant.id,
        'username': applicant.username,
        'email': applicant.email,
        'bio': applicant.bio,
        # 'skills': [{'id': skill.id, 'name': skill.name} for skill in applicant.skills],
        'skills': [skill.name for skill in applicant.skills],
        'values': [value.name for value in applicant.values],
    }

def _validate_field(data, field, proceed, errors, missing_okay=False):
    # can't create a user if there is no unique email
    # or if email field is empty
    if field in data:
        if len(data[field]) == 0:
            proceed = False
            errors.append(f"required '{field}' parameter is blank")
    if not missing_okay and field not in data:
        proceed = False
        errors.append(f"required '{field}' parameter is missing")
        data[field] = ''

    return proceed, data[field], errors

def _add_attribute(model, attribute_id, applicant_id):
    if model == ApplicantSkill:
        attribute = ApplicantSkill(skill_id=attribute_id, applicant_id=applicant_id)
    elif model == ApplicantValue:
        attribute = ApplicantValue(value_id=attribute_id, applicant_id=applicant_id)

    db.session.add(attribute)
    db.session.commit()

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

    def post(self, *args, **kwargs):
        applicant, errors = self._create_applicant(json.loads(request.data))

        if applicant is not None:
            applicant_payload = _applicant_payload(applicant)
            applicant_payload['success'] = True
            return {
                'success': True,
                'data': applicant_payload
            }, 201
        else:
            return {
                'success': False,
                'error': 400,
                'errors': errors
            }, 400

    def _create_applicant(self, data):
        # helper method to create applicant and add to DB
        proceed = True
        errors = []

        proceed, email, errors = _validate_field(
            data, 'email', proceed, errors)

        if proceed:
            applicant = Applicant(
                email=email,
                first_name=data['first_name'],
                last_name=data['last_name'],
                bio=data['bio'],
                username=data['username']
            )
            db.session.add(applicant)
            db.session.commit()

            [_add_attribute(ApplicantSkill, skill_id, applicant.id) for skill_id in data['skills']]
            [_add_attribute(ApplicantValue, value_id, applicant.id) for value_id in data['values']]

            return applicant, errors
        else:
            return None, errors



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
