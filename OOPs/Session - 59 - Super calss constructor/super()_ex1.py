class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display1(self):
        print('Person Name:',self.name)
        print('Person Age:',self.age)
        
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
        
    def display2(self):
        #super().display()
        print('Person Name:',self.name)
        print('Person Age:',self.age)
        print('Rollno:',self.rollno)
        print('Marks:',self.marks)


s=Student('Aditya',35,101,98)
s.display2()
