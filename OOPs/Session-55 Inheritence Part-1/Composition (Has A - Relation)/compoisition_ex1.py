class Engine:
    a=10
    def __init__(self):
        self.b=10
    def m1(self):
        print('Engine specific functionality')

class Car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print('class car using engine Functionality')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()

c=Car()
c.m2()
