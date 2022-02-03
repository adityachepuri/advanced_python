# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:16:38 2020

@author: ADITYA
"""


from threading import *
import time
import random
import queue
def produce(q):
    while True:
        item=random.randint(1,100)
        print('Producer producing item:',item)
        q.put(item)
        print('Producer givving notification')
        time.sleep(5)

def consume(q):
    while True:
        print('Consumer waiting for updation')
        print('Consumer consuming item:',q.get())
        time.sleep(5)

q=queue.Queue()
t1=Thread(target=consume,args=(q,))
t2=Thread(target=produce,args=(q,))
t1.start()
t2.start()