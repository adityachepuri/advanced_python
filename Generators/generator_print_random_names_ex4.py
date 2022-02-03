from random import *
import time
names=['Aditya','Anuiketh','Shreeram','Madhu']
subjects=['Python','Java','Blockchain','DJango']
def people_list(num):
    results=[]
    for i in range(num):
        person={'id':i,'name':choice(names),'subjects':choice(subjects)}
        results.append(person)
    return results
print(people_list(3))
