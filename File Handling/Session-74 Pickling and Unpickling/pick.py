import emp,pickle
f=open("emp.dat","wb")
n=int(input("Enter no.of employees"))
for i in range(n):
    eno=int(input("Enter Employee Number:"))
    ename=input("Enter Employee Name:")
    esal=int(input("Enter salary:"))
    e=emp.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
