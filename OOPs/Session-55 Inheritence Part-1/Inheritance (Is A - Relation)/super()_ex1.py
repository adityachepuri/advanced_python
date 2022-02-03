class C:
    a=10
    def __init__(self):
        self.b=20

class D(C):
    c=30
    def __init__(self):
        super().__init__()
        self.d=40

c=D()
print(c.a,c.b,c.c,c.d)
