import numpy as np
import matplotlib.pyplot as plt
ori = np.pi/4
x = np.linspace(0,1,1000)
def f(x):
    return 1/(1+x*x)
y_real = f(x)


def tra(f,n,a=0,b=1):
    h = (b-a)/n; fa = f(a); fb = f(b)
    summ = 0; X = [a]; Y = [fa]
    for i in range(1,n):
        x = a + i*h; y = f(x)
        summ = summ + y
        X.append(x); Y.append(y)
    X.append(b); Y.append(fb)
    return (h/2)*(fa+fb+(2*summ)), X, Y

j = 10#For better result set j = 1 or maybe 2
print("______________________________________________")
print("N","         ","Approx Int","         ","Error")
print("______________________________________________")
for i in range(5):
    s,X,Y = tra(f,j)
    error = ori-s
    print(" ",j,"   ",s,"  ",error)
    plt.plot(x,y_real)
    for k in range(j):
        xs = [X[k],X[k],X[k+1],X[k+1]]
        ys = [0,f(X[k]),f(X[k+1]),0]
        plt.fill_between(xs,ys)
    j = 2*j
    plt.show()
