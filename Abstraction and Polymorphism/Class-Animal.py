# import necessary packages
from abc import ABC, abstractmethod
# create a base class
class Animal(ABC):

    # abstractmethod
    # should be implemented by all sub-classes
    def move(self):
        pass

# sub classes
class Human(Animal):

    def move(self):
        print("I can walk and run1")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("i can roar")

# driver code

r = Human()
r.move()

k = Snake()
k.move()

r = Dog(
r.move()

k = Lion()
k.move()
