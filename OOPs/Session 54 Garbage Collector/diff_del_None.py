import time
class Test:
    def __init__(self):
        print("Object initializating...")
    def __del__(self):
        print("Fulfilling last wish and performing cleanup activities")

t1=Test()
del t1
#t=None
print(id(t1))
