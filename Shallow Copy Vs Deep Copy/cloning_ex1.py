l1=[10,20,30,40]
l2=l1.copy()
l2[2]=70
print('l1:',l1)
print(id(l1))
print()
print('l2:',l2)
print(id(l2))
print()

print('Cloning concept to check whether objects are same are not')
l1=[10,20,30,40]
l2=l1
l2[2]=70
print('l1:',l1)
print(id(l1))
print()
print('l2:',l2)
print(id(l2))
print()
