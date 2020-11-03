import json
import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models import Skill

class GetSkillsTest(unittest.TestCase):
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

class GetAllSkillsTest(GetSkillsTest):
    def test_get_all_skills(self):
        skill1 = Skill(name='skill 1')
        db.session.add(skill1)
        skill2 = Skill(name='skill 2')
        db.session.add(skill2)

        response = self.client.get(
            f'/api/v1/skills'
        )
        self.assertEqual(200, response.status_code)

        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(2, len(data['data']))
        self.assertEqual('skill 1', data['data'][0]['attribute'])
        self.assertEqual('skill 2', data['data'][1]['attribute'])
