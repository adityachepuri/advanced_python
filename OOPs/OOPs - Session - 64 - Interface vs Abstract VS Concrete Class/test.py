class Test():
    __x=10
    def __init__(self):
        self.__y=20

t=Test()
print(t.__dict__)
print(Test.__dict__)
print(Test._Test__x)
print(t._Test__y)
