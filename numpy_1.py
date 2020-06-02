import numpy as np
a=np.array([1,2,3])
#print(a)
b=np.arange(500,1000,100)
c=np.array([4,4,4,4])
#c=np.append(c,[2])
for i in range(5):
    c=np.append(c,[i],axis=0)
#np.append([3],0)
print(c)
