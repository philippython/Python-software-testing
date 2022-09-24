# #  destructing variables
# from unicodedata import name
# from abc import ABC , abstractmethod

# t = [3, 5,6, 7, 2, 6]

# *_, x, y = t 

# class ClassTest:
    
#     def instance_method(self):
#         print(f"Called instance_method of {self}")

#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
        
#     @staticmethod
#     def static_method():
#         print("Called static_method")



# # test = ClassTest()
# # test.instance_method()
# ClassTest.class_method()
# ClassTest.static_method()

# class Book:

#     TYPES = ("hardcover", "paperback")

#     def __init__(self, name, booktype, weight):
#         self.name = name
#         self.booktype = booktype
#         self.weight = weight

#     def __repr__(self):
#         return f"<Book {self.name}, {self.booktype}, {self.weight}g>"

# book = Book("A thousand years", "hardcover", 450)
# print(book)

# # Python program showing
# # abstract base class work

# from abc import ABC, abstractmethod

# class Polygon(ABC):

# 	@abstractmethod
# 	def noofsides(self):
# 		pass

# class Triangle(Polygon):

# 	# overriding abstract method
# 	def noofsides(self):
# 		print("I have 3 sides")

# class Pentagon(Polygon):

# 	# overriding abstract method
# 	def noofsides(self):
# 		print("I have 5 sides")

# class Hexagon(Polygon):

# 	# overriding abstract method
# 	def noofsides(self):
# 		print("I have 6 sides")

# class Quadrilateral(Polygon):

# 	# overriding abstract method
# 	def noofsides(self):
# 		print("I have 4 sides")

# # Driver code
# R = Triangle()
# R.noofsides()

# K = Quadrilateral()
# K.noofsides()

# R = Pentagon()
# R.noofsides()

# K = Hexagon()
# K.noofsides()

name = 'philip'
#  declaring a function
# def hello():
#     print("Hello Everyone")

# #  calling a function
# hello()

# price = 49
# txt = "The price is {} dollars"

# def age(year, name):
#     # parameter
#     # f string 
#     age = 2022 - year
#     print(f'{name} is {age} years old')
#     'emmanuel is 19 years old'
#     f'emmanuel is {80 - 70}'
#     f'philip is owing 780'

# age(2003, 'emmanuel')




print('Welcome to temperature converter')
temperature = input("What's the current temperature. e.g 50K or 50F  ")
def temperature_converter(currrent_temperature):
    #  datatype conversion or type casting
    if currrent_temperature.endswith('K') or  currrent_temperature.endswith('k') : return -273.15 + float(currrent_temperature[0:-1]) 
    if currrent_temperature.endswith('F') or currrent_temperature.endswith('f') : return (int(currrent_temperature[0:-1]) - 32) * 5/9


answer = round(temperature_converter(temperature), 2)
print(answer)







