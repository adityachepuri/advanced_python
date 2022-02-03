import csv
with open('emp.csv','w') as f:
    w=csv.writer(f)
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    n=int(input('Enter no.of employees:'))
    for i in range(n):
        eno=int(input('Enter employee number:'))
        ename=input('Enter name of the employee:')
        esal=float(input('Enter employee salary'))
        eaddr=input('Enter Employee address')
        w.writerow([eno,ename,esal,eaddr])
print('Total employees data written to CSV file successfully')
