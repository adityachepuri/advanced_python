class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        print('add method calling')
        total=self.pages + other.pages
        return Book(total)

    def __str__(self):
        print('str method is calling...')
        return str(self.pages)

b1=Book(100)
b2=Book(200)
b3=Book(300)
b4=Book(400)
b5=Book(100)

type(print(b1+b2+b3+b4+b5)
#print(type(bx))
#print(bx.pages)
#print(type(bx.pages))
#print('sum of b1+b2+b3+b4',b1+b2+b3+b4)
#print(type(('sum of b1+b2+b3+b4',b1+b2+b3+b4)))
