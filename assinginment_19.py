import numpy as np

a = np.array([1,2,3])
print(type(a))                        #type nunmpy .b=ndarrary
print(a.shape)
print(a[0],a[1],a[2])                 #print
a[0] = 5
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)                              #colums and rows
print(b[0,0],b[0,1],b[1,0])                 #b00, b01, b10 elements



import numpy as np
a = np.array((2,2))
print(a)
b = np.ones((1,2))
print(b)
c = np.full((2,2),7)
print(c)
d = np.eye(2)
print(d)

e = np.random.random((2,2))
print(e)
print(type(e))
