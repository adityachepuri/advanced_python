class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def carinfo(self):
        print("\t Name is {} \t Model is {} \t Color is {}".format(self.name,self.model,self.color))
        
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat_n_drink(self):
        print('Eat Biryani and drink beer')

class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        self.car=car

    def work(self):
        print('Coding in Python')

    def empinfo(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.esal)
        print("Car info:",self.car)
        self.car.carinfo()
        
c=Car('Innova','2.5V','Grey')
e=Employee('Aditya',35,423,10000,c)
e.eat_n_drink()
e.work()
e.empinfo()
