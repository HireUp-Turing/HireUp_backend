# import pdb; pdb.set_trace()
import datetime
import json

from flask import request
from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Applicant

# HELPER METHODS
def _search_results_payload(filtered_applicants):

    return {
        'id': applicant.id,
        'username': applicant.username,
        'email': applicant.email,
        'bio': applicant.bio,
        'skills': [skill.name for skill in applicant.skills],
        'values': [value.name for value in applicant.values],
    }

def _create_sql_query(skill_ids, value_ids):
    sql_query = "SELECT DISTINCT applicants.* FROM applicants JOIN applicant_skills ON applicants.id = applicant_skills.applicant_id JOIN applicant_values ON applicants.id = applicant_values.applicant_id WHERE "
    skill_ids_length = len(skill_ids) - 1
    value_ids_length = len(value_ids) - 1
    if skill_ids and value_ids:
        for skill_id in skill_ids:
            sql_query = sql_query + f"applicant_skills.skill_id = {skill_id} OR "
        for value_id in value_ids:
            if value_id != value_ids[value_ids_length]:
                sql_query = sql_query + f"applicant_values.value_id = {value_id} OR "
            else:
                sql_query = sql_query + f"applicant_values.value_id = {value_id}"
        return sql_query
    elif skill_ids and not value_ids:
        for skill_id in skill_ids:
            if skill_id != skill_ids[skill_ids_length]:
                sql_query = sql_query + f"applicant_skills.skill_id = {skill_id} OR "
            else:
                sql_query = sql_query + f"applicant_skills.skill_id = {skill_id}"
        return sql_query
    elif value_ids and not skill_ids:
        for value_id in value_ids:
            if value_id != value_ids[value_ids_length]:
                sql_query = sql_query + f"applicant_values.value_id = {value_id} OR "
            else:
                sql_query = sql_query + f"applicant_values.value_id = {value_id}"
        import pdb; pdb.set_trace()
        return sql_query

#### NEXT STEPS
    # render error when no ids passed at all (line 73)
    # make sure non-erroneous input renders correctly
## add error handling for when "skills" and/or "values" JSON body keys are not present

class SearchResultsResource(Resource):
    """
    this Resource file is for our /applicants/search endpoint
    """

    def get(self, **kwargs):
        skill_ids = request.json['skills']
        value_ids = request.json['values']
        sql_query = _create_sql_query(skill_ids, value_ids)
        if not skill_ids and not value_ids:
            return {
                'success': Flase,
                'error': "error code",
                'errors': "error messages"
            }, "error code"
        else:
            filtered_applicants = db.engine.execute(sql_query)
            search_results_payload = _search_results_payload(filtered_applicants)
            return {
                'success': True,
                'data': search_results_payload
            }, 200
