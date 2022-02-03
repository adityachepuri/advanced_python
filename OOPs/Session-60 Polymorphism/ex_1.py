class Duck:
    def talk(self):
        print('Quack Quack...')

class Dog:
    def talk(self):
        print('Bhow Bhow...')

class Cat:
    def talk(self):
        print('Meow Meow..')

class Goat:
    def talk(self):
        print('Myah Myah...')

def f1(self):
    obj.talk()

l=[Duck(),Dog(),Cat(),Goat()]
for obj in l:
    f1(obj)
