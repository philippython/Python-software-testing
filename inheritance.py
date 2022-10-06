from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def func1(self):
        pass

    def func2(self):
        print('This is a parent class')


class Child(Parent): 
    def func1(self):
        print('This is a child class')


class Developer:

    def __init__(self, name, exp, level):
        self.level = level
        self.exp = exp
        self.name = name

    @classmethod
    def senority_level(cls, name, exp):
        return cls(name, exp, "senior" if exp > 3 else 'junior')

    

philip = Developer.senority_level('john', 8)
print(philip.level)