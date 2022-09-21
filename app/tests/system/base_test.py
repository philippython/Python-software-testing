import unittest
from app import app

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.testing = True
        self.client = app.test_client()