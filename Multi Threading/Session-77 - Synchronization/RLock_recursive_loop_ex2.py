from threading import *
import time
l=RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result=1
        l.release()
    else:
        result=n*factorial(n-1)
        l.release()
    return result

def result(n):
    print('The factorial of',n,'is:',factorial(n))
t1=Thread(target=result,args=(5,))
t2=Thread(target=result,args=(9,))
t1.start()
t2.start()
