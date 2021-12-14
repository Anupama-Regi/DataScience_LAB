# 3. Write Python program to create two matrices (read values from user) and find the Trace
import numpy as np
r=int(input("Enter the dimension of square matrix : "))
c=r
print("Enter",r*r,"elements : ")
a=list(map(int,input().split()))
if len(a)!=r*c:
  print("Enter correct number of elements ! ! ! ")
else :
  matrix=np.array(a).reshape(r,c)
  print("\nMatrix : \n",matrix)
  print("\n\nTrace of the matrix : ",np.trace(matrix))
