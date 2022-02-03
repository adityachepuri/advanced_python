class Test:
    def __init__(self):
        print("no-arg constructor")

    def __init__(self,x):
        print("one-arg constructor")

    def __init__(self,x,y):
        print("two-arg constructor",x,y)

t1=Test(30,40)
