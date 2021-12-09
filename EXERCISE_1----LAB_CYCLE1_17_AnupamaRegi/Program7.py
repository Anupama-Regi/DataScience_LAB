#PROGRAM - 7 : NumPy Program to save a given array to a text file and load it ?
import numpy as np
import os
a1=np.arange(20,40).reshape(5,4)
print("\nGiven array is :\n\n",a1)
np.savetxt('text1.txt',a1,fmt='%d',header='matrix')
result=np.loadtxt('text1.txt')
print("\n Result is :\n\n",result)