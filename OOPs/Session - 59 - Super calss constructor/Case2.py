class P:
    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3(self):
        print('Parent static method')

class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        
    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

c=C()
c.m1()
