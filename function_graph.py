import matplotlib.pyplot as plt
import numpy as np

n = int(input("Give me number of functions = "))
print("Give me the equation (If use numpy then say numpy nato gaar mara) = ")
E = []
for i in range(n):
	eq = input("f(%s)"%(i))
	E.append(eq)

x1 = float(input("Give the lower limit of x = "))#2
x2 = float(input("Give the upper limit of x = "))#-2
y1 = float(input("Give the lower limit of y = "))#-1
y2 = float(input("Give the upper limit of y = "))#10

color = ['red','blue','green','black']
axes = plt.gca()
axes.set_ylim([y1,y2])
x = np.arange(x1,x2,0.001)
for i in range(n):
	Y = eval(E[i])
	plt.plot(x,Y,c=color[i],label='f(x) = %s'%E[i])
plt.legend(loc='best',prop={'size':12})
plt.xlabel("x")
plt.ylabel("functions")
plt.title(" Sumit er chu")
plt.show()

