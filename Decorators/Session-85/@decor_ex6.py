def decor1(func):
    def inner1():
        print('Decor1 enhanced function')
    return inner1

@decor1
def f1():
    print('Original Function')

f1()
