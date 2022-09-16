from typing import List

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

print(a)
print(b)

a = 567
b = 567

print(id(a), id(b))

class Student:
    def __init__(self, name: str, grades : List[int] = []):
        self.names = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)