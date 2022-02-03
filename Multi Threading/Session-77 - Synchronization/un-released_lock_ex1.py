from threading import *
l=Lock()
l.acquire()
print('Main Thread acquiring lock...')
l.release()
print('Main Thread lock released...')
l.release()
