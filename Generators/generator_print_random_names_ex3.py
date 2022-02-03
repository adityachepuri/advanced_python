from random import *
import time
def namegenerator():
    alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:
        name=' '
        for i in range(6):
            name=name+choice(alphabets)
        yield name

for i in namegenerator():
    time.sleep(3)
    print(i)
