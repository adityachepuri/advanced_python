from threading import *
def job():
    print('Child Thread')

t=Thread(target=job)
print(current_thread().getName)
print(t.daemon)
t.setDaemon(True)
print(t.daemon)
