class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def __str__(self):
        return ('This is the student with name {} and with rollno: {}'.format(self.name,self.rollno))

s1=Student('Durga',101)
s2=Student('Aditya',102)
print(s1)
print(s2)
