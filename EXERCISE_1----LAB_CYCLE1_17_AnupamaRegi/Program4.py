#PROGRAM - 4 : NumPy Program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15 ?
import numpy as np
a1=np.arange(21)
print("\n Array is : \n\n",a1)
a1[(a1 >=9)&(a1<=15)]*=-1
print("\n Matrix after changing the sign of the numbers in the range from 9 to 15: \n\n",a1)
