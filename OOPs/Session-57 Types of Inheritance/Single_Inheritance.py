## SIngle Inheritance Method ##

class P:
    def m1(self):
        print('Parent method')

class C(P):
    def m2(self):
        print('Child method')

c=C()
c.m1()
c.m2()
