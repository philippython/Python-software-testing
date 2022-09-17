from unittest import TestCase
import unittest
from post import Post

class PostTest(TestCase):
    def setUp(self):
        self.post = Post("TestTitle", "TestContent")

    def test_post_init_(self):
        self.assertEqual(self.post.title, "TestTitle")
        self.assertEqual(self.post.content, "TestContent")

    def test_post_json(self):
        data = {
            "title" : "TestTitle",
            "content" : "TestContent"
        }
        self.assertDictEqual(self.post.json(), data)


if __name__ == "__main__":
    unittest.main()