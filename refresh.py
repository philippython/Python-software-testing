#  destructing variables
from unicodedata import name
from abc import ABC , classmethod

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

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()
