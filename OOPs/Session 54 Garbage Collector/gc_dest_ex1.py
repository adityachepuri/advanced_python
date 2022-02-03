import time
class Test:
    def __init__(self):
        print("Object Initialization....")

    def __del__(self):
        print("Fulfilling last wish and performing cleanup activities....")

t1=Test()
print("Using t1 based on our requirement")
time.sleep(5)
print("Work with t1 completed, eligible for GC")
t1=None
time.sleep(10)
print('End of application')
