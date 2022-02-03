from threading import *
l=Lock()
l.acquire()
print('Main Thread acquiring lock...')
l.acquire()
print('Main Thread lock released...') ## Cannot this execute this line 
l.release()
