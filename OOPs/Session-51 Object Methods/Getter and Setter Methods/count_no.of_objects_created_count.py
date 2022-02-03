## WAP to create no.of objects created for a class ##

class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noOfObjectsCreated(cls):
     print('The number of objects created:',Test.count)

t1=Test()
t2=Test()
t3=Test()
Test.noOfObjectsCreated()
t4=Test()
t5=Test()
Test.noOfObjectsCreated()
