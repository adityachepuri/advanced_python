class P1:
    def m1(self):
        print('Parent method')

class P2:
    def m2(self):
        print('Child method')

class C(P1,P2):
    def m3(self):
        pass

c=C()
c.m1()
c.m2()
c.m3()
