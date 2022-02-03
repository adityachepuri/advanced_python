from abc import *

class Vehicle(ABC):
    @abstractmethod
    def get_no_of_wheels(self):
        pass

class Bus(Vehicle):
    def get_no_of_wheels(self):
        return 7

class Auto(Vehicle):
    def get_no_of_wheels(self):
        return 3

b=Bus()
print(b.get_no_of_wheels())

a=Auto()
print(a.get_no_of_wheels())
