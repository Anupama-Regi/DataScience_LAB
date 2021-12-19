#3.Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title

import matplotlib.pyplot as plt
with open("text2.txt") as f:
    data=f.read() 
data=data.split(',')
x=[i.split(' ')[0] for i in data]
y=[i.split(' ')[1] for i in data]
plt.plot(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Graph')
plt.show()