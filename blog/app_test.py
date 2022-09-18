import app
from blog import Blog
import unittest
from unittest.mock import patch
from app import MENU_PROMPT


class AppTest(unittest.TestCase):
    def setUp(self):
        self.blog = Blog("TestBlog", "TestAuthor")

    def test_print_blog(self):
        app.blogs = {"Test" : self.blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- TestBlog by TestAuthor (0 post)')

    def test_menu_prompt(self):
        with patch("builtins.input") as mocked_input :
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

if __name__ == "__main__":
    unittest.main()