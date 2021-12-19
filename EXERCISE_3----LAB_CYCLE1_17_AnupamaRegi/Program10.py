"""10. Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science.
Use marks of 10 students.
Sample data:
Test Data:
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] """

import matplotlib.pyplot as plt
math_marks=[88,92,80,89,100,80,60,100,80,34]
science_mark=[35,79,79,48,100,88,32,45,20,30]
marks_range=[10,20,30,40,50,60,70,80,90,100]
plt.scatter(marks_range,math_marks,label="Maths marks",color="blue")
plt.scatter(marks_range,science_mark,label="Science marks",color="red")
plt.legend(loc='upper right')
plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")
plt.title("Scatter plot")
plt.show()