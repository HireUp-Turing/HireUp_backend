from flask_restful import Resource, abort
from sqlalchemy.orm.exc import NoResultFound

from api import db
from api.database.models import Value

# Serializer
def _value_payload(value):
    return {
        'id': value.id,
        'attribute': value.name
    }

class ValuesResource(Resource):
    """
    /values
    """

    def get(self, *args, **kwargs):
        values = Value.query.all()
        results = [_value_payload(value) for value in values]

        return {
            'success': True,
            'data': results
        }, 200
