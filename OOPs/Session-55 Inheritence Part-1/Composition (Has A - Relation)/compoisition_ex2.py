class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def getInfo(self):
        print('Car Name',self.model)
        print('Model',self.model)
        print('Car Color',self.color)


class Employee:

    def __init__(self,eno,ename,car):
        self.eno=eno
        self.ename=ename
        self.car=car

    def empInfo(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Car Information....')
        self.car.getInfo()

car=Car('Innova','2.5V','Grey')
emp=Employee(100,'Aditya',car)
emp.empInfo()
