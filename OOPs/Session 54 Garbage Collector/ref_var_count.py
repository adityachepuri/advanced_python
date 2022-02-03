import sys
class Test:
    pass

t1=Test()
t2=t1
t3=t1
t4=t1
del t2
print(sys.getrefcount(t1))
