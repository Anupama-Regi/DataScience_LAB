#4. Write a Python program to plot two or more lines on same plot with suitable legends of each line

import matplotlib.pyplot as plt
x1=[10,25,30]
y1=[20,25,10]
plt.plot(x1,y1,label="line 1")
x2=[10,15,20,30]
y2=[40,15,10,30]
plt.plot(x2,y2,label="line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends of each line')
plt.legend()
plt.show()