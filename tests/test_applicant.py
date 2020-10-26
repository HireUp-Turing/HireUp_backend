import unittest
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.database.models import Applicant

# api.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost/database1"


class AppTest(unittest.TestCase):
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

    def test_applicant_model(self):
        gaby = Applicant(email='gaby@hireup.com', first_name='Gaby', last_name='Mendez')
        db.session.add(gaby)
        db.session.commit()

        self.assertIsInstance(gaby, Applicant)
        self.assertIsNotNone(gaby.id)
        self.assertEqual(1, gaby.id)
        self.assertEqual('gaby@hireup.com', gaby.email)
        self.assertEqual('Gaby', gaby.first_name)
        self.assertEqual('Mendez', gaby.last_name)




# import unittest
#
# import app
#
# def test_test():
#     assert app.test() == "Works!"
