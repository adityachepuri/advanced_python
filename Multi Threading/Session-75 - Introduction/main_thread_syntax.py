from threading import*
def display():
    print('This code(display function) is executed by thread:',current_thread().getName())
t=Thread(target=display)
t.start()
print('This code is executed by Thread:',current_thread().getName())
