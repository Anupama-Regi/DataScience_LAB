#PROGRAM - 8 : NumPy Program to check whether two arrays are equal (element wise) or not ?
import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[11,2,30],[4,51,6]])
print("\nTwo given arrays are :\n\n")
print("\nFirst Array :\n\n",a1)
print("\nSecond Array :\n\n",a2)
print("\nEquals OR Not using---- == ---- :\n\n",a1==a2)
print("\nEquals OR Not using---- equals ---- :\n\n",np.equal(a1,a2))