from threading import *
l=RLock()
print('Main thread is trying to Lock')
l.acquire()
print('Main thread is trying to acquire lock again....')
l.acquire()
print('Main thread acquire same lock again..')
