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
        self.networth = 0

    @property
    def worth(self):
        return self.networth

    @worth.setter
    def worth(self, worth):
        if worth > 75:
            return "Worth is too high"
        self.networth = worth


    @classmethod
    def senority_level(cls, name, exp):
        return cls(name, exp, "senior" if exp > 3 else 'junior')

    @staticmethod
    def gender(name):
        return "male" if name[0] in ('j', 'p', 'm') else "female"
            
        


john = Developer.senority_level('john', 8)
print(john.worth)

print(dir(Developer))
