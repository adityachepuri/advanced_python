# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 23:34:35 2020

@author: ""ADITYA""

"""


from threading import *
import time
s=Semaphore()
def wish(name):
    s.acquire()
    for i in range(5):
        print('Good Evening:',name)
        time.sleep(2)
    s.release()
t1=Thread(target=wish,
          args=('Dhoni',))
t2=Thread(target=wish,args=('Yuvraj',))
t3=Thread(target=wish,args=('Kohli',))
t4=Thread(target=wish,args=('Rohit',))
t5=Thread(target=wish,args=('Pandya',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

