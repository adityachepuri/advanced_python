import emp,pickle
f=open("emp.dat","rb")
print("Employee Details")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
        print()
    except EOFError:
        print("All Employees Completed")
        break
f.close()
