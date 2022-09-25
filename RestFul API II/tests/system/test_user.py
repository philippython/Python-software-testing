from models.user import UserModel
from tests.base_test import BaseTest
import unittest , json

class UserTest(BaseTest):
    
    def test_register_user(self):
        data = {
            'username' : 'Test',
            'password' : 'Test1234'
        }
        with self.test_client() as client:
            response = client.post('/register', data)
            self.assertEqual(response.status_code, 201)
            
    def test_login_user(self):
        pass        





if __name__ == "__main__":
    unittest.main()