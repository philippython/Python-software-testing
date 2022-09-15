#  destructing variables
from unicodedata import name


t = [3, 5,6, 7, 2, 6]

*_, x, y = t 

class ClassTest:
    
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
        
    @staticmethod
    def static_method():
        print("Called static_method")

# test = ClassTest()
# test.instance_method()
ClassTest.class_method()
ClassTest.static_method()

class Book:

    TYPES = ("hardcover", "paperback")

    def __init__(self, name, booktype, weight):
        self.name = name
        self.booktype = booktype
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.booktype}, {self.weight}g>"

book = Book("A thousand years", "hardcover", 450)
print(book)

