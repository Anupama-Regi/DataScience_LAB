# 1. Write Python program to create two matrices (read values from user) and find the Dot Product
import numpy as np
def readmatrix():
  r=int(input("Enter the number of rows : "))
  c=int(input("Enter the number of columns : "))
  print("Enter",r*c,"entries in a single line (separated by space): ")
  a=list(map(int, input().split()))
  if len(a)!=r*c:
    print("Enter correct number of elements ! ! ! ")
  else :
    matrix=np.array(a).reshape(r,c)
    #print("Matrix : \n",matrix)
    return(matrix)
m1=readmatrix()
m2=readmatrix()
if np.shape(m1)(1)==np.shape(m2)(0):
  print("\nMatrix 1 :\n",m1)
  print("\nMatrix 2 :\n",m2)
  print("\n\nDot Product : \n",np.dot(m1,m2))
else:
  print("\nNumber of columns of matrix1 must be equal to number of rows of matrix2 ! ! !")
