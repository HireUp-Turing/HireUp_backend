import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant

# HELPER METHODS
def _search_results_payload(applicants):

    return {
        'id': applicant.id,
        'username': applicant.username,
        'email': applicant.email,
        'bio': applicant.bio,
        'skills': [skill.name for skill in applicant.skills],
        'values': [value.name for value in applicant.values],
    }

def _find_applicants_with_skill(skill_id):
    return db.engine.execute(f"SELECT DISTINCT applicants.* FROM applicants JOIN applicant_skills ON applicants.id = applicant_skills.applicant_id WHERE applicant_skills.skill_id = {skill_id};")


class SearchResultsResource(Resource):
    """
    this Resource file is for our /applicants/search endpoint
    """

    def get(self, **kwargs):
        skill_ids = request.json['skills']
        value_ids = request.json['values']
        applicants_results = []
        # set empty search results array
        # if skills array and values array both have contents
        if skill_ids and value_ids:
            import pdb; pdb.set_trace()
            for skill_id in skill_ids:
                applicant_results.append(_find_applicants_with_skill(skill_id))
            # iterate over skills ids to find applicants with each skill
            # push resulting collection of applicants into search results array
            # iterate over values ids to find applicants with each value
            # push resulting collection of applicants into search results array
            # unique the resulting collection of applicants
        # if skills array empty and values array has contents
        elif skill_ids and not value_ids:
            import pdb; pdb.set_trace()

            # ^^ do the above just with values array
        # if values array empty and skills array has contents
        elif value_ids and not skill_ids:
            import pdb; pdb.set_trace()
            # ^^ do the above just with skills array
        else:
            import pdb; pdb.set_trace()
        # if both arrays empty
            # error



        applicants = db.engine.execute(f"SELECT DISTINCT applicants.* FROM applicants JOIN applicant_skills ON applicants.id = applicant_skills.applicant_id WHERE applicant_skills.skill_id = {skill_id};")
