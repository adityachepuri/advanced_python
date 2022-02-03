class Student:
    '''This is a practice program developed by Aditya'''
    def __init__(self):
        self.name='Aditya'
        self.age=30
        self.marks=80

    def talk(self):
        print("Hello I'm fine:",self.name)
        print("My age is:",self.age)
        print("my marks:",self.marks)
s=Student()
print(s.name) # As the print function is not mentioned 
print(s.age)
print(s.marks)
s.talk()

