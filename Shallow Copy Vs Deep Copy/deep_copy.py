## Example for Deep Copy ##

import copy
l1=[10,20,30,[40,50],60]
l2=copy.deepcopy(l1)
l1[0]=999
l1[3][1]=777
print()
print(l1)
print(id(l1))
print()
print(l2)
print(id(l2))

#Note: Deep copy can create a copy of nested list as well
