"""6. Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity           : 22.2  17.6    8.8  8           77  6.7
(iii) Write a Python programming to display a bar chart of the popularity of programming Languages.Use different color for each bar."""

import numpy as np
import matplotlib.pyplot as plt
data={'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':77,'C++':6.7}
color=["red","blue","cyan","yellow","green","maroon"]
courses=list(data.keys())
data1=list(data.values())
plt.bar(courses,data1,color=color)
plt.xlabel("Programming languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming languages")
plt.show()