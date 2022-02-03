def decor1(func):
    def inner1():
        x=func()
        return x*x
    return inner1

def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor1
@decor
def num():
    return 10
print(num())

@decor
@decor1
def num():
    return 10
print(num())
