# import necessary Modules
from abc import ABC, abstractmethod

# create base class 
class Absclass(ABC):

    # Function to print a value
    def print(self,x):
        print("Passed value: ", x)

    # Abstract method
    @abstractmethod
    def task(self):
        print("we are inside ABsclass task")

# create sub class
class test_class(Absclass):
    def task(self):
        print("we are inside test_class task")

#objectof test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)