class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.display()

    def display(self):
        print('Hi',self.name)
        print('Your marks are:',self.marks)
        self.grade()

    def grade(self):
        if self.marks >= 60:
            print('You got First Grade')
        elif self.marks >=50:
            print('You got a second Grade')
        elif self.marks >=35:
            print('You got Third Grade')
        else:
            print('Better luck Next time')

s=Student('Aditya',95)
s1=Student('Shreeram',90)
s2=Student('Akshay',85)
s3=Student('XYZ',34)
