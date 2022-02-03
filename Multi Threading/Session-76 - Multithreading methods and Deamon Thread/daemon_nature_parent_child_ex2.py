from threading import *
import time
def job():
    for i in range(10):
        print('Lazy Method')
        time.sleep(2)

t=Thread(target=job)
t.setDaemon(True)
t.start()
#time.sleep(5)
print('End of Main Thread')
