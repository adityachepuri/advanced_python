import time
class Test:
    def __init__(self):
        print('Object initialization....')

    def __del__(self):
        print("Fulfilling last wish and performing cleanup activities..")

list=[Test(),Test(),Test()]
del list
time.sleep(5)
print('End of application')
