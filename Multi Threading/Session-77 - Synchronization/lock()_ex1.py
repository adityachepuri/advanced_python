from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(5):
        print('Hello {},{}'.format('Good Evening',name))
        time.sleep(2)
    #l.release()

t1=Thread(target=wish,args=('Aditya',))
t2=Thread(target=wish,args=('Shreeram',))
t3=Thread(target=wish,args=('Aniketh',))
t1.start()
t2.start()
t3.start()
time.sleep(25)
print('Main thread wont require lock....')
print(t1.is_alive())
