import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant, Skill, Value

def _options_payload(skills, values):

    return {
        'skills': [{'id': skill.id, 'attribute': skill.name} for skill in skills],
        'values': [{'id': value.id, 'attribute': value.name} for value in values]
    }
