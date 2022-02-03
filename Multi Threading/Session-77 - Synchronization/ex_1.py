from threading import *
import time
def wish(name):
    for i in range(10):
        print('Good Evening')
        time.sleep(2)
        print(name)

wish('Shreeram')
