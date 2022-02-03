from threading import *
def display():
    print('Child Thread')
t=Thread(target=display)
t.start()
print('Main thread identification number:',current_thread().ident)
print('Child thread identification number:',t.ident)
