from threading import*
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print('Child Thread-1',end=' ')

t=MyThread()
t.start()
for i in range(10):
    print('Main Method-1 ')
