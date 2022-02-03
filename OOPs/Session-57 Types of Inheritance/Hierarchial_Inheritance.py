## Hierarchial Inheritance ##

class P:
    def m1(self):
        print('Parent method')

class C1(P):
    def m2(self):
        print('Child method')

class C2(P):
    def m3(self):
        print('sub child method')

c1=C2()
c1.m1()
c1.m3()
c1.m2() # Mentioned just for reference. It give error
        # AttributeError: 'C2' object has no attribute 'm2'
