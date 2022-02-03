def decor(func):
    def inner():
        print('Enhanced Function')
        func()
    return inner

@decor
def f1():
    print('Original Function')

f1()
