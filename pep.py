from typing import List, Optional

def search(sequence: List, expected:  str, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(f"{store.name} - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "%s, total stock price: %s" % (store.name, store.stock_price)


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)


#  type hinting


Store.franchise(store)  
Store.franchise(store2)   
Store.store_details(store)  
Store.store_details(store2)


# Custome erorr classes
class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    

    def __repr__(self) -> str:
        return "<Book %s, read %s pages out of %s" % (self.name, self.pages_read, self.page_count)

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count :
            raise TooManyPagesReadError(
                'You tried to read {} out of {} pages'.format(self.pages_read + pages, self.page_count)
                )
        self.pages_read += pages
        print("You have now read %s pages out of %s" % (self.pages_read, self.page_count))


python101 = Book("Python 101", 50)
python101.read(45)
python101.read(5)

# first class functions
friends = [
    {"name": "adedamola"},
    {"name": "john"},
    {"name": "james"}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "john", get_friend_name))

# mutability in python

a = []
b = a

b.append(35)

# print(a)
# print(b)

a = 567
b = 567

# print(id(a), id(b))

# mutable default parameters
class Student:
    def __init__(self, name: str, grades : Optional[List[int]] = None):
        self.names = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)

#  singleton : method 1
class Singleton:

    __instance = None

    @staticmethod # used for creating utility static_method with self or cls as parameters
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton already exist")
        else:
            Singleton.__instance = self


s1 = Singleton.get_instance()
s1.x = 5
print(s1)
s2 = Singleton.get_instance()
print(s2.x)

