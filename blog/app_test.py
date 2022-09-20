import app
from blog import Blog
import unittest
from unittest.mock import patch
from app import MENU_PROMPT

class AppTest(unittest.TestCase):

    def test_menu_prompt(self):
        with patch("builtins.input") as mocked_input :
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog("TestBlog", "TestAuthor")
        app.blogs = {"Test" : blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- TestBlog by TestAuthor (0 post)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input_blogs : 
            mocked_input_blogs.side_effect = ('TestBlog', 'TestAuthor')
            app.ask_to_create_blog()

            self.assertIsNotNone(app.blogs.get('TestBlog'))


if __name__ == "__main__":
    unittest.main()


