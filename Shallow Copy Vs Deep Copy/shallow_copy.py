## Example for Shallow Copy ##

import copy
l1=[10,20,30,[40,50],60]
l2=copy.copy(l1)
l1[0]=999
l1[3][1]=777
print()
print(l1)
print(id(l1))
print()
print(l2)
print(id(l2))

#Note: Shallow copy cannot create a duplicate object for nested list
