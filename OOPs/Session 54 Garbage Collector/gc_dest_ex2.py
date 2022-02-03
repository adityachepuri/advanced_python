import time
class Test:
    def __init__(self):
        print("Object initializating...")
    def __del__(self):
        print("Fulfilling last wish and performing cleanup activities")

t1=Test()
t2=t1
t3=t2
time.sleep(5)
del t1
print("Object not destroyed after deleting t1")
time.sleep(5)
del t2
print("Object not destroyed after deleting t2")
del t3
time.sleep(5)
print("End od application")
