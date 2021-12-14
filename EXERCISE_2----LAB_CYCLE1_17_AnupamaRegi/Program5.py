# 5. Write Python program to create two matrices (read values from user) and find the Determinant
import numpy as np
r=int(input("Enter the number of row of matrix : "))
c=int(input("Enter the number of columns of matrix : "))
print("Enter",r*c,"elements : ")
a=list(map(int,input().split()))
if len(a)!=r*c:
  print("Enter correct number of elements ! ! ! ")
else :
  matrix=np.array(a).reshape(r,c)
  print("\nMatrix : \n",matrix)
  print("\n\nDeterminant of the matrix : ",np.linalg.det(matrix))
