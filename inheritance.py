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
