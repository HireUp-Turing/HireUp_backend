import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Message

def _message_payload(message):

    return {
        'id': message.id,
        'applicant_id': message.applicant_id,
        'employer_name': message.employer_name,
        'employer_email': message.employer_email,
        'body': message.body,
        'read_status': message.read_status,
        'created_at' : message.created_at.__str__()
    }

def _validate_field(data, field, proceed, errors, missing_okay=False):
    # can't create a user if there is no unique email
    # or if email/values/skills fields are empty
    if field in data:
        if len(data[field]) == 0:
            proceed = False
            errors.append(f"required '{field}' parameter is blank")
    if not missing_okay and field not in data:
        proceed = False
        errors.append(f"required '{field}' parameter is missing")
        data[field] = ''

    return proceed, data[field], errors

def _validate_id_field(data, field, proceed, errors, missing_okay=False):
    # validation for integer field (like id)
    if field in data:
        if type(data[field]) != int:
            proceed = False
            errors.append(f"required '{field}' must be an integer")
    if not missing_okay and field not in data:
        proceed = False
        errors.append(f"required '{field}' parameter is missing")
        data[field] = ''

    return proceed, data[field], errors

class MessagesResource(Resource):
    """
    this Resource file is for our /messages endpoints
    which don't require a resource ID in the URI path
    """

    def get(self, *args, **kwargs):
        applicant_id = request.args.get('applicant_id')

        if applicant_id:
            messages = db.session.query(Message).filter_by(applicant_id=applicant_id).all()
        else:
            messages = Message.query.all()

        results = [_message_payload(message) for message in messages]
        return {
            'success': True,
            'data': results
        }, 200

    def post(self, *args, **kwargs):
        message, errors = self._create_message(json.loads(request.data))

        if message is not None:
            message_payload = _message_payload(message)
            message_payload['success'] = True
            return {
                'success': True,
                'data': message_payload
            }, 201
        else:
            return {
                'success': False,
                'error': 400,
                'errors': errors
            }, 400

    def _create_message(self, data):
        proceed = True
        errors = []

        # employer info can't be blank
        proceed, employer_name, errors = _validate_field(
            data, 'employer_name', proceed, errors)
        proceed, employer_email, errors = _validate_field(
            data, 'employer_email', proceed, errors)
        proceed, applicant_id, errors = _validate_id_field(
            data, 'applicant_id', proceed, errors)

        if proceed:
            message = Message(
                applicant_id=applicant_id,
                employer_name=employer_name,
                employer_email=employer_email,
                body=data['body']
            )
            db.session.add(message)
            db.session.commit()

            return message, errors
        else:
            return None, errors

class MessageResource(Resource):
    """ single message Show:
    GET /messages/:id
    """
    def get(self, *args, **kwargs):
        # kwargs == params

        message_id = kwargs['message_id']
        message = None
        try:
            message = db.session.query(Message).filter_by(id=message_id).one()
        except NoResultFound:
            return abort(404)

        return {
            'success': True,
            'data': _message_payload(message)
        }, 200
