import unittest
from app import app
import json

class TestHome(unittest.TestCase):

    def test_home_route(self):
        with app.test_client() as client:
            response = client.get('/')
            expected = {"message" : "HelloWorld"}

            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()), expected)


if __name__ == "__main__":
    unittest.main()