def decor2(func):
    def inner2():
        print('Decor2 enhanced function')
        func()
    return inner2

def decor1(func):
    def inner1():
        print('Decor1 enhanced function')
        func()
    return inner1

@decor2
@decor1
def f1():
    print('Original Function')

f1()
