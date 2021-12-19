"""6. Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity             22.2  17.6    8.8  8           77  6.7
(i) Write a Python program to display a bar chart  of the popularity of programming Languages."""

import numpy as np
import matplotlib.pyplot as plt
data={'Java':22.2,'Python':17.6,'PHP':8.8,'JavaScript':8,'C#':77,'C++':6.7}
courses=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,5))
plt.bar(courses,values,color='c',width=.5)
plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()