from threading import *
import time
def display():
    print(current_thread().name,'Started...')
    time.sleep(3)
    print(current_thread().name,'Ended...')
print('The number of active threads:',active_count())
t1=Thread(target=display,name='Child Thread 1')
t2=Thread(target=display,name='Child Thread 2')
t3=Thread(target=display,name='Child Thread 3')
t1.start()
t2.start()
t3.start()
print('The number of actve threads:',active_count())
time.sleep(10)
print('The number of active threads:',active_count())
