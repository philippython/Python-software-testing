import unittest
from tests.base_test import BaseTest

class ItemModelTest(BaseTest):

    def test_find_by_name(self):
        with self.app_context():
            item = self.model("Test", 78.99)
           
            self.assertIsNone(item.find_by_name("Test"))

            item.save_to_db()
            response = item.find_by_name("Test")

            self.assertEqual(response.name, "Test")
            self.assertEqual(response.price, 78.99)
            self.assertIsNotNone(response)

            item.delete_from_db()
            self.assertIsNone(item.find_by_name("Test"))

            






















if __name__ == "__main__":
    unittest.main()