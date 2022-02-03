class A:
    def m1(self):
        print("A Class Method")

class B:pass
   # def m1(self):
        #print("B class method")

class C:pass
    #def m1(self):
        #print("C Class method")

class D(B,C): pass
    # def m1(self):
        # print("D class method")

d=D()
d.m1()
