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

# singleton : method 2

class NewSingleton:

    __instance = None

    def __new__(cls):
        if (cls.__instance is None ):
            cls.__instance = \
                super(NewSingleton, cls).__new__(cls)
        return cls.__instance

s3 = NewSingleton()
print(s3)
s3.pop = 50
s4 = NewSingleton()
print(s4)
print(s4.pop)


gradeclass = {}
studentNames = ['Bett James','Namukolo Abrams','Vera Abutu','Kwame Doga','Lukeman Ahmad','Akin Torey','Luke Brant','James Kenyata', 'Ngugi Tionga', 'Okoro Eze','Agatha Chiluba','Mangu Joseph','Longe Jethro', 'Florence Giwa','Vetiva Lucent','Melody Braimoh','Victor Ihab', 'Mimi Trucker','Maguel Peter','Wellington Zuba']
overallAvgScore = [63.00157894736842, 51.76940789473684, 57.342302631578946, 60.579407894736846, 53.46059210526316, 48.07993421052632, 51.831907894736844, 56.24243421052631, 43.8053947368421, 53.96157894736842, 70.59842105263158, 43.672302631578944, 76.48993421052631, 55.686052631578946, 49.37282894736842, 52.17282894736842, 51.422302631578944, 55.52092105263158, 42.02434210526316, 46.07006578947368]
gradePiont = ['A','B','C','D','E','F']
gradeStatus = ['Pass','Fail','Retake']

gradeclassifier = []

for score in overallAvgScore:
    if score > 76.00: gradeclassifier.append("A")
    if score < 76 and score >= 66 : gradeclassifier.append("B")
    if score < 66 and score >= 56 : gradeclassifier.append("C")
    if score < 56 and score >= 51 : gradeclassifier.append("D")
    if score == 50 : gradeclassifier.append("E")
    if score < 50 : gradeclassifier.append("F")

grades = {}
for i in range(0, len(gradeclassifier)):
    if gradeclassifier[i] == "F":
        grades[studentNames[i]] = [gradeclassifier[i], "Fail"]
    elif gradeclassifier[i] == "E":
        grades[studentNames[i]] = [gradeclassifier[i], "Retake"]
    else:
        grades[studentNames[i]] = [gradeclassifier[i], "Pass"]

print(grades)







