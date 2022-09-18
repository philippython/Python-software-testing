import app
from blog import Blog
import unittest
from unittest.mock import patch


class AppTest(unittest.TestCase):
    def setUp(self):
        self.blog = Blog("TestBlog", "TestAuthor")

    def test_print_blog(self):
        app.blogs = {"Test" : self.blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- TestBlog by TestAuthor (0 post)')


if __name__ == "__main__":
    unittest.main()