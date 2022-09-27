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




# print('Welcome to temperature converter')
# temperature = input("What's the current temperature. e.g 50K or 50F  ")
# def temperature_converter(currrent_temperature):
#     #  datatype conversion or type casting
#     if currrent_temperature.endswith('K') or  currrent_temperature.endswith('k') : return -273.15 + float(currrent_temperature[0:-1]) 
#     if currrent_temperature.endswith('F') or currrent_temperature.endswith('f') : return (int(currrent_temperature[0:-1]) - 32) * 5/9


# answer = round(temperature_converter(temperature), 2)
# print(answer)




# """
# This assessment is to test your knowlegde of python dictionaries and functions and a lot more
# - I used some advanced string formating in the code below, check them out on google to understand how the work and try to use them in your code some other time
# - This code is a demo bank application
# - The dictionary stores users and bank officials information like password and users account balance
# - You need to understand how the dictionary is structured before attempting to debug this code
# - The code below checks if the a user is logging in with the right information/details
# - And shows the user balance
# - A bank official can also login
 
#  +++ Hint 
#  Run the code first before attempting to debug 
# Happy coding and debugging !!!
# """
# print("""
#                         ░░░░                      
#                     ░░░░  ░░░░                    
#                     ░░░░░░░░░░                    
#                         ░░░░                      
                                                  
#           ▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  
#           ▒▒░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒              
#           ▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒            
#         ▒▒░░░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒            
#         ▒▒░░██░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
#     ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒        
#     ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒  ▒▒    
#     ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒      
#       ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
#         ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
#           ▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒            
#             ▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒              
#             ▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒              
#             ▒▒▒▒▒▒            ▒▒▒▒▒▒              
                                                  
                                                  
# ██████████████████████████████████████████████████
# """)
# bank_model = {
#     "officials" : {
#         # you can choose to change name afterwards
#         0 : {
#             "name" : "Danile Vanek",
#             "password": "dv000"
#         } ,
#         1 : {
#             "name" : "Donald Dorcas",
#             "password": "dd001"
#         }
#     },
#     "customers":{
#         "0123456789" : {
#             "account_type": "current",
#             "account_name": "John Kennedy",
#             "balance": 250,
#             "password" : "jk002"
#         },
#         "0444456789" : {
#             "account_type": "current",
#             "account_name": "richard james",
#             "balance": 1250,
#             "password" : "rj003"
#         },
#     }
# }

# def login():
#     print("Welcome to TEEKAY Bank")
#     user = int(input("Log in as a bank 0fficial or a bank user? Enter 1. for official 2. for user "))

#     if user == 1 :
#         id = int(input("Enter your official id: "))
#         password = input("Enter your official password: ")

#         if password ==  bank_model["officials"][id]["password"]: 
#             msg = "Welcome back %s " % (bank_model["officials"][id]["name"])
#             print(msg)

#         elif password !=  bank_model["officials"][id]["password"]:
#             print("password or id is invalid!!")
#             login()
#     else:
#         id = input("Enter your account number: ")
#         password = input("Enter your account password: ")
    
#         if password ==  bank_model["customers"][id]["password"]:
#             msg = "Welcome back %s\n Your current balance: $%s" % (bank_model["customers"][id]["account_name"], bank_model['customers'][id]["balance"])
#             print(msg)

#         elif password !=  bank_model["customers"][id]["password"]:
#             print("password or id is invalid!!")
#             login()

# login()

"""
This assessment is to test your knowlegde of python dictionaries and functions and a lot more

- I used some advanced string formating in the code below, check them out on google to understand how the work and try to use them in your code some other time
- This code is a demo bank application
- The dictionary stores users and bank officials information like password and users account balance
- You need to understand how the dictionary is structured before attempting to debug this code
- The code below checks if the a user is logging in with the right information/details
- And shows the user balance
- A bank official can also login
 
 +++ Hint 
 Run the code first before attempting to debug 
Happy coding and debugging !!!

"""
print("""
                        ░░░░                      
                    ░░░░  ░░░░                    
                    ░░░░░░░░░░                    
                        ░░░░                      
                                                  
          ▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  
          ▒▒░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒              
          ▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒            
        ▒▒░░░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒            
        ▒▒░░██░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
    ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒        
    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒  ▒▒    
    ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒      
      ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
        ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒          
          ▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒            
            ▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒              
            ▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒              
            ▒▒▒▒▒▒            ▒▒▒▒▒▒              
                                                  
                                                  
██████████████████████████████████████████████████
""")
bank_model = {
    "officials" : {
        # you can choose to change name afterwards
        0 : {
            "name" : "Danile Vanek",
            "password": "dv000",
            
        } ,
        1 : {
            "name" : "Donald Dorcas",
            "password": "dd001",
            
        }
    },
    "customers":{
        "0123456789" : {
            "account_type": "current",
            "account_name": "John Kennedy",
            "balance": 250,
            "password" : "jk002"
        },
        "0444456789" : {
            "account_type": "current",
            "account_name": "richard james",
            "balance": 1250,
            "password" : "rj003"
        },
    }
}

def login():
    print("Welcome to TEEKAY Bank")
    user = int(input("Log in as a bank 0fficial or a bank user? Enter 1. for official 2. for user "))

    if user == 1 :
        id = int(input("Enter your official id: "))
        password = input("Enter your official password: ")

        if password ==  bank_model["officials"][id]["password"] :
            msg = "Welcome back %s " % (bank_model["officials"][id]["name"])
            print(msg)

        elif password !=  bank_model["officials"][id]["password"]:

            print("password or id is invalid!!")
            login()
    else:
        id = input("Enter your account number: ")
        password = input("Enter your account password: ")
    
        if password ==  bank_model["customers"][id]["password"] :
            msg = "Welcome back %s\n Your current balance: $%s" % (bank_model["customers"][id]["account_name"], bank_model['customers'][id]["balance"])
            print(msg)

        elif password !=  bank_model["customers"][id]["password"]:
            print("password or id is invalid!!")
            login()

login()
