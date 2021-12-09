#PROGRAM - 10 : NumPy Program to multiply two given arrays of same size element by element ?
import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[11,2,30],[4,51,6]])
print("\nTwo given arrays are :\n\n")
print("\nFirst array :\n\n",a1)
print("\nSecond array :\n\n",a2)
print("\n\nAfter multiplication of same size matrix element by element : \n\n",np.multiply(a1,a2))