from unittest import TestCase
import unittest

from models.item import ItemModel

class TestItem(TestCase):

    def setUp(self):
        self.item = ItemModel("Test", 45.00)

    def test_create_item(self):
        
        self.assertEqual(self.item.name, "Test")
        self.assertEqual(self.item.price, 45.00)

    def test_item_json(self):
        expected = {'name': 'Test', 'price': 45.00}

        self.assertDictEqual(self.item.json(), expected)

if __name__ == "__main__":
    unittest.main()