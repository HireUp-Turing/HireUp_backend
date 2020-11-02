import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant, Skill, Value

# HELPER METHODS
def _applicant_payload(applicant):

    return {
        'id': applicant.id,
        'username': applicant.username,
        'email': applicant.email,
        'bio': applicant.bio,
        'skills': [skill.name for skill in applicant.skills],
        'values': [value.name for value in applicant.values],
    }

def _filter_applicants(skill_ids, value_ids):
    if skill_ids and value_ids:
        applicants = None
    elif skill_ids and not value_ids:
        applicants = db.session.query(Applicant).join(Skill, Applicant.skills).filter(Skill.id.in_(skill_ids))
    elif value_ids and not skill_ids:
        applicants = db.session.query(Applicant).join(Value, Applicant.values).filter(Value.id.in_(value_ids))
    return applicants

class SearchResultsResource(Resource):
    """
    this Resource file is for our /applicants/search endpoint
    """

    def get(self, **kwargs):
        skill_ids = request.json['skills']
        value_ids = request.json['values']

        if not skill_ids and not value_ids:
            return {
                'success': False,
                'error': 400,
                'errors': "At least one skill or value id must be specified in order to filter applicant search results."
            }, 400
        ### will come back to building out this error condition later
        # elif skill_ids is None or value_ids is None:
        #     return {
        #         'success': False,
        #         'error': 400,
        #         'errors': "skill_ids and value_ids keys must be present in request body."
        #     }, 400
        else:
            # filtered_applicants = db.engine.execute(sql_query)
            # search_results = [_applicant_payload(applicant) for applicant in filtered_applicants]
            filtered_applicants = _filter_applicants(skill_ids, value_ids)
            search_results = [_applicant_payload(applicant) for applicant in filtered_applicants]
            return {
                'success': True,
                'data': search_results
            }, 200





# def _create_sql_query(skill_ids, value_ids):
#     sql_query = "SELECT DISTINCT applicants.* FROM applicants JOIN applicant_skills ON applicants.id = applicant_skills.applicant_id JOIN applicant_values ON applicants.id = applicant_values.applicant_id WHERE "
#     skill_ids_length = len(skill_ids) - 1
#     value_ids_length = len(value_ids) - 1
#     if skill_ids and value_ids:
#         for skill_id in skill_ids:
#             sql_query = sql_query + f"applicant_skills.skill_id = {skill_id} OR "
#         for value_id in value_ids:
#             if value_id != value_ids[value_ids_length]:
#                 sql_query = sql_query + f"applicant_values.value_id = {value_id} OR "
#             else:
#                 sql_query = sql_query + f"applicant_values.value_id = {value_id}"
#         return sql_query
#     elif skill_ids and not value_ids:
#         for skill_id in skill_ids:
#             if skill_id != skill_ids[skill_ids_length]:
#                 sql_query = sql_query + f"applicant_skills.skill_id = {skill_id} OR "
#             else:
#                 sql_query = sql_query + f"applicant_skills.skill_id = {skill_id}"
#         return sql_query
#     elif value_ids and not skill_ids:
#         for value_id in value_ids:
#             if value_id != value_ids[value_ids_length]:
#                 sql_query = sql_query + f"applicant_values.value_id = {value_id} OR "
#             else:
#                 sql_query = sql_query + f"applicant_values.value_id = {value_id}"
#         return sql_query
