import numpy as np
a=np.array([[1,2,3],[1,2,3]])
print(a)
print(a.shape)

b=np.zeros((2,1))
print(b)

b=np.ones((3,3))
print(b)

b=np.full((3,4),4)
print(b)

b=np.eye(2)
print(b)

b=np.random.random((2,2))
print(b)

c=np.array([[1,2,3,4,6],[7,8,9,10,11],[12,13,14,15,16]])
print(b)

print(c[0,3],c[1,3],c[2,3])
print(c[0,1],c[1,1],c[2,1])
print(c[0,2],c[1,2],c[2,2])