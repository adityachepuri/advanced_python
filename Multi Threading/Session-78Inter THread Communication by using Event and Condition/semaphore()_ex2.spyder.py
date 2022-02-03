# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 00:21:29 2020

@author: Aisin R&D
"""


from threading import *
s=Semaphore(2)
s.acquire()
print('Acquiring first time')
s.acquire()
print('Acquiring second time')
s.acquire()
print('Acquiring Third time')