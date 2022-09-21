import unittest
from app import app

class TestHome(unittest.TestCase):

    def test_home_route(self):
        with app.test_client() as client:
            response = client.get('/')
            expected = {"message" : "HelloWorld"}
            self.assertDictEqual(dict(response) , expected)


if __name__ == "__main__":
    unittest.main()