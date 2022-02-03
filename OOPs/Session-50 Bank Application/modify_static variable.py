class Test:
    a=10
    def __init__(self):
        self.a=888

t=Test()
print(t.a)
print(Test.a)
