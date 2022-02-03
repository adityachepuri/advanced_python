class Test:
    a=10
    def __init__(self):
        Test.a=999
        
    def m1(self):
        Test.a=222
print(Test.a)
t=Test()
print(Test.a)
print(m)
