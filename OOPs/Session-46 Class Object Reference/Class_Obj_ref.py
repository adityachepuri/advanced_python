class Employee:
    def __init__(self,ename,eno,esal,eadd):
        self.ename=ename
        self.eno=eno
        self.esal=esal
        self.eadd=eadd

    def display(self):
        print("Name of the employee:",self.ename)
        print("Employee ID is:",self.eno)
        print("Salary is:",self.esal)
        print("Address is:",self.eadd)

print('****************************************')

e1=Employee('Aditya',100,30000,'Hyderabad')
e1.display()
print()

print('****************************************')

e2=Employee('Shreeram',200,50000,'Bangalore')
e2.display()
