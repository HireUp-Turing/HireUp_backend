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
        'read_status': message.created_at,
        'created_at' : message.created_at
    }

class MessagesResource(Resource):
    """
    this Resource file is for our /messages endpoints
    which don't require a resource ID in the URI path
    """

    def get(self, *args, **kwargs):
        messages = Message.query.all()
        results = [_message_payload(message) for message in messages]
        return {
            'success': True,
            'data': results
        }, 200

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
