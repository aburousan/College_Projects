import numpy as np
import matplotlib.pyplot as plt

def bessel(n,x):
	y0 = 1; y1 = x+1 ; i=2
	if n == 0:
		return y0
	elif n==1:
		return y1
	else:
		while i<=n:
			r = ((2*i-1)*x*y1) + y0
			y0 = y1
			y1 = r
			i = i+1
		return y1
x1 = float(input("Give the lower limit of x = "))
x2 = float(input("Give the upper limit of x = "))
X = np.arange(x1,x2,0.01)

n = int(input("Give the value of n = "))
plt.plot(X,bessel(n,X),c='red',label='n = %d'%n)
plt.title("Bessel Function")
plt.legend(loc='best',prop={'size':12})
plt.xlabel("x")
plt.ylabel("Bessel")
plt.show()