import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Skill

# HELPER METHODS
def _skill_payload(skill):

    return {
        'id': skill.id,
        'name': skill.username
    }

class SkillsResource(Resource):
    """
    /skills
    """

    def get(self, *args, **kwargs):
        skills = Skill.query.all()
        results = [_skill_payload(skill) for skill in skills]

        return {
            'success': True,
            'data': results
        }, 200
