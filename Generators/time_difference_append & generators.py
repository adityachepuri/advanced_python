from random import *
import time 
names=['Aditya','Aniketh','Shreeram','Madhu']
subjects=['Python','Java','Django','Blockchain']
def people_list(num):
    results=[]
    for i in range(num):
        person={'id':i,'name':choice(names),'subjects':choice(subjects)}
        results.append(person)
    return results

def people_generators(num):
    results=[]
    for i in range(num):
        person={'id':i,'name':choice(names),'subjects':choice(subjects)}
        yield person

t1=time.time()
people=people_generators(100000)
t2=time.time()
print('Time taken:',t2-t1)
