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

    def __init__(self, exp):
        self.senority = self.senority_level()
        self.exp = exp

    @classmethod
    def senortiy_level(cls, exp):
        return "senior" if exp > 3 else 'junior' 

philip = Developer(7)
print(philip.exp)