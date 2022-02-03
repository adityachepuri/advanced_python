from threading import*
class Test:
    def display(self):
        for i in range(10):
            print('Child Thread-1',end=' ')

obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print('Main Method-2 ')
    
