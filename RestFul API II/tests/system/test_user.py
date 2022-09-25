from models.user import UserModel
from tests.base_test import BaseTest
import unittest , json

class UserTest(BaseTest):
    
    def test_register_user(self):
        data = {'username' : 'Test','password' : 'Test1234'}
        headers = { "content-Type": "application/json"}
        with self.test_client() as client:
            with self.app_context() :
                response = client.post('/register', data=json.dumps(data), headers=headers)
                self.assertEqual(response.status_code, 201)
                self.assertDictEqual(json.loads(response.data), {"message": "User created successfully."})

    def test_login_user(self):
        pass        

    def test_register_duplicate_user(self):
        pass




if __name__ == "__main__":
    unittest.main()