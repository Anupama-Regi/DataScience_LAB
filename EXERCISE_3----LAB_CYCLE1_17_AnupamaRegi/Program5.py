#5. Write a Python program to create multiple plots.

import matplotlib.pyplot as plt
figure,axis=plt.subplots(2,2)
x1=[10,30]
y1=[10,30]
axis[0,0].plot(x1,y1)
axis[0,0].set_title("Plot 1")
x2=[10,10]
y2=[30,50]
axis[0,1].plot(x2,y2)
axis[0,1].set_title("Plot 2")
x3=[30,10]
y3=[10,30]
axis[1,0].plot(x3,y3)
axis[1,0].set_title("Plot 3")
x4=[10,30]
y4=[10,10]
axis[1,1].plot(x4,y4)
axis[1,1].set_title("Plot 4")
plt.show()