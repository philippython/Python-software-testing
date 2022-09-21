import unittest
from .base_test import BaseTest
import json

class TestHome(BaseTest):

    def test_home_route(self):
        with self.client as client:
            response = client.get('/')
            expected = {"message" : "HelloWorld"}

            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()), expected)


if __name__ == "__main__":
    unittest.main()