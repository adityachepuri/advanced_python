from threading import *
import time
def display():
    for i in range(10):
        print('Seetha Thread')
        time.sleep(3)
t=Thread(target=display)
t.start()
t.join(10)
for i in range(10):
    print('Rama Thread')
