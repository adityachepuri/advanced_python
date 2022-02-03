import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)

with open("emp.dat","wb") as f:
    e=Employee('100','Aditya','1000','Hyd')
    pickle.dump(e,f)
    print('Pickling of employee object completed...')

with open('emp.dat','rb') as f:
    obj=pickle.load(f)
    print("Employee information after unpickling...")
    obj.display()
    print(obj)
