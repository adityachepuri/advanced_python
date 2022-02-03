from threading import *
import time
def display():
    print(current_thread().name,'Started...')
    time.sleep(3)
    print(current_thread().name,'Ended....')
    print(current_thread().isDaemon)
    
t1=Thread(target=display,name='Child Thread 1')

t2=Thread(target=display,name='Child Thread 2')

t3=Thread(target=display,name='Child Thread 3')

t1.start()
t2.start()
t3.start()
print(t1.name,'Is Alive:',t1.is_Alive())
print(t2.name,'Is Alive:',t2.is_Alive())
print(t3.name,'Is Alive:',t3.is_Alive())
time.sleep(10)
print(t1.name,'Is Alive:',t1.is_Alive())
print(t2.name,'Is Alive:',t2.is_Alive())
print(t3.name,'Is Alive:',t3.is_Alive())
