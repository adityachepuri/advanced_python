### C3 Algorithm / Samuel Pedroni Algorithm / DLR Algorith ###


class A:pass
    #def m1(self):
        #print('A class method')

class B:pass
    #def m1(self):
        #print('B calss method')

class C:
    def m1(self):
        print('C class method')

class X(A,B):pass
    #def m1(self):
        #print('X class method')

class Y(B,C):pass
    #def m1(self):
        #print('Y calss method')

class P(X,Y,C):pass
    #def m1(self):
        #print('P class method')

p=P()
p.m1()
