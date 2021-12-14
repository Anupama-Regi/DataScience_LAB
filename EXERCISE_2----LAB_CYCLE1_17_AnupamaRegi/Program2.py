# 2. Write Python program to create two matrices (read values from user) and find the Transpose
import numpy as np
r=int(input("Enter the number of rows : "))
c=int(input("Enter the number of columns : "))
print("Enter",r*c,"elements one by one using space : ")
a=list(map(int,input().split()))
if len(a)!=r*c:
    print("Enter correct number of elements ! ! ! ")
else :
  matrix=np.array(a).reshape(r,c)
  print("\nMatrix : \n",matrix)
  print("\n\nTransposed Matrix : \n",np.transpose(matrix))
