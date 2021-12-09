#PROGRAM - 6 : NumPy Program to compute sum of all elements,sum of each column and sum of each row of a given array ?
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\nGiven array is :\n\n",a1)
print("\n Sum of all elements :\n\n",np.sum(a1))
print("\n Sum of each columns :\n\n",np.sum(a1,axis=0))
print("\n Sum of each rows :\n\n",np.sum(a1,axis=1))
