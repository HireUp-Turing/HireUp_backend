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
        skills = db.engine.execute("SELECT DISTINCT skills.id, skills.name FROM applicant_skills JOIN applicants ON applicants.id = applicant_skills.applicant_id JOIN skills ON applicant_skills.skill_id = skills.id ORDER BY skills.name")

        values = db.engine.execute("SELECT DISTINCT values.id, values.name FROM applicant_values JOIN applicants ON applicants.id = applicant_values.applicant_id JOIN values ON applicant_values.value_id = values.id ORDER BY values.name")

        options = {"skills": skills, "values": values}

        results = [_options_payload(options)]

        return {
            'success': True,
            'data': results
        }
