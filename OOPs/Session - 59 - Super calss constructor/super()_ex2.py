class P:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print('Parent Instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    a=888
    def __init__(self):
        self.b=999

        print("Instance variable 'b' in calss C",self.b)
        super().__init__() # If we donot use super() we can access the variable in the child class
        print(super().a)
        print(self.b)
        super().m1()
        super().m2()
        super().m3()

c=C()
print('The vale of b in child class is:',c.b)
