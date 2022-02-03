from threading import *
import time
import random
items=[]
def produce(c):
    while True:
        c.acquire()
        item=random.randint(1,100)
        print('Producer is producing item:',item)
        items.append(item)
        print('Producer giving notification')
        c.notify()
        c.release()
        time.sleep(5)

def consume(c):
    while True:
        c.acquire()
        print('Consumer is waiting for updation')
        c.wait()
        print('Consumer is consuming item:',items.pop())
        c.release()
        time.sleep(5)
c=Condition()
t1=Thread(target=consume,args=(c,))
t2=Thread(target=produce,args=(c,))
t1.start()
t2.start()
