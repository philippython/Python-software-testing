"""
BaseTest

This class ahould be the parent class to each non-unit test.
it alllows for instantation of the dynamics dynamically
and makes sure that it is a new, blank address each time.


"""
from db import db
from unittest import TestCase
from app import app
from models.item import ItemModel
import unittest

class BaseTest(TestCase):
    def setUp(self):
        """
        make sure databse exists and get test_client
        """
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get test client
        self.client = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        """make sure databse is erased"""
        with app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()