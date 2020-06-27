import numpy as np
import matplotlib.pyplot as plt

ori = np.pi/4
def f(x):
	return 1/(1+(x*x))
x_real = np.linspace(0,1,1000)
y_real = f(x_real)

def traezoid(f,n,a=0,b=1):
    x = np.linspace(a,b,n+1)
    y = f(x); h = (b - a)/n
    y_last = y[1:];y_first = y[:-1]
    s = (h/2) * np.sum(y_first + y_last)
    return s, x, y
    
j = 2#For better result set j = 1 or maybe 2
print("______________________________________________")
print("N  \t Approx Integration. \t Error")
print("______________________________________________")
for i in range(4):
    s,X,Y = traezoid(f,j)
    error = ori-s
    print("{0:6.0f}".format(j),"\t","{0:1.12f}".format(s),"\t ","{0:1.12e}".format(error))
    plt.subplot(2,2,i+1)
    plt.plot(x_real,y_real,label='n = %s'%j)
    plt.legend(loc='best')
    for k in range(j):
        xs = [X[k],X[k],X[k+1],X[k+1]]
        ys = [0,f(X[k]),f(X[k+1]),0]
        plt.fill_between(xs,ys)
    j = j*2
plt.show()
