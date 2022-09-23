import unittest
from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('Test').save_to_db()
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))
    
    def test_model_relationship(self):
        with self.app_context():
            StoreModel('Test').save_to_db()
            ItemModel('test', 19.99, 1).save_to_db()

            store_item = ItemModel.query.filter_by(store_id=1).first()

            self.assertIsNotNone(store_item)
            self.assertEqual(store_item.name, 'test')
            self.assertEqual(store_item.price, 19.99)
            self.assertEqual(store_item.id, 1)


if __name__ == "__main__":
    unittest.main()