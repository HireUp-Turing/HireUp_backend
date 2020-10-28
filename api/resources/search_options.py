import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant, Skill, Value

def _options_payload(options):

    return {
        'skills': [{'id': skill.id, 'attribute': skill.name} for skill in options['skills']],
        'values': [{'id': value.id, 'attribute': value.name} for value in options['values']]
    }

class SearchOptionsResource(Resource):
    """
    this Resource file is for our /search-options endpoints
    """

    def get(self, *args, **kwargs):
        skills = Skill.query.all()
        values = Value.query.all()
        options = {"skills": skills, "values": values}

        results = [_options_payload(options)]

        return {
            'success': True,
            'data': results
        }
