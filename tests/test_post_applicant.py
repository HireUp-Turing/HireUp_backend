import json
import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models import Skill, Value, Applicant

class PostApplicantTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_new_applicant(self):
        skill = Skill(name='skill')
        db.session.add(skill)
        value = Value(name='value')
        db.session.add(value)

        new_data = {
            'email': 'gaby@hireup.com',
            'username': 'giraffes',
            'bio': 'this is a test bio',
            'first_name': 'gaby',
            'last_name': 'mendez',
            'skills': [1],
            'values': [1]
        }

        response = self.client.post(
            '/api/v1/applicants', json=new_data,
            content_type='application/json'
        )
        self.assertEqual(201, response.status_code)

        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(1, data['data']['id'])
        self.assertEqual(['skill'], data['data']['skills'])
