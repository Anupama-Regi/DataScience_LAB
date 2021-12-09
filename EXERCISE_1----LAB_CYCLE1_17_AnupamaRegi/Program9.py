#PROGRAM - 9 : NumPy Program to create a 4*4 array with random values,now create a new array from the said array swapping first and last rows ?
import numpy as np
a1=np.arange(16).reshape(4,4)
print("\n4*4 array with random values is :\n\n",a1)
a1[[0,3]]=a1[[3,0]]
print("\nNew array after swaping first and last rows :\n\n",a1)