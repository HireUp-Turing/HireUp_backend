import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant

def _search_results_payload(applicants):

    return {
        'id': applicant.id,
        'username': applicant.username,
        'email': applicant.email,
        'bio': applicant.bio,
        'skills': [skill.name for skill in applicant.skills],
        'values': [value.name for value in applicant.values],
    }

class SearchResultsResource(Resource):
    """
    this Resource file is for our /applicants/search endpoint
    """

    def get(self, **kwargs):
        import pdb; pdb.set_trace()
        # set empty search results array
        # if skills array and values array both have contents
            # iterate over skills ids to find applicants with each skill
            # push resulting collection of applicants into search results array
            # iterate over values ids to find applicants with each value
            # push resulting collection of applicants into search results array
            # unique the resulting collection of applicants
        # if skills array empty and values array has contents
            # ^^ do the above just with values array
        # if values array empty and skills array has contents
            # ^^ do the above just with skills array
        # if both arrays empty
            # error
        # end

        skill_ids = request.json['skills']
        value_ids = request.json['values']

        applicants = db.engine.execute(f"SELECT DISTINCT applicants.* FROM applicants JOIN applicant_skills ON applicants.id = applicant_skills.applicant_id WHERE applicant_skills.skill_id = {skill_id};")
