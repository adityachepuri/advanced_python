from threading import *
import time
def display():
    print(current_thread().name,'Started....')
    time.sleep(3)
    print(current_thread().name,'Ended....')
t1=Thread(target=display,name='Child Thread 1')
t2=Thread(target=display,name='Child Thread 2')
t3=Thread(target=display,name='Chi;d Thread 3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for z in l:
    print('Name:',z.name)
