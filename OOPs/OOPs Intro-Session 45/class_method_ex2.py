class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        print(id(self))

    def talk(self):
        print("hello my name is:",self.name)
        print("My rollno is:",self.rollno)
        print("My marks are:",self.marks)
        print(id(self))
print()
s1=Student("Aditya",101,90)
print(id(s1))
s1.talk()



print()
s2=Student("Shreeram",102,95)
s2.talk()
