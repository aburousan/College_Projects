import numpy as np
import matplotlib.pyplot as plt

def legen(n,x):
	p0 = 1; p1 = x ; i=2
	if n == 0:
		return p0
	elif n==1:
		return p1
	else:
		while i<=n:
			r = (((2*i-1)*x*p1)-((i-1)*p0))/i
			p0 = p1
			p1 = r
			i = i+1
		return p1

x1 = float(input("Give the lower limit of x = "))
x2 = float(input("Give the upper limit of x = "))
X = np.arange(x1,x2,0.01)

n = int(input("Give the value of n = "))
plt.plot(X,legen(n,X),c='red',label='n = %d'%n)

plt.title("Legendre Polynomial")
plt.legend(loc='best',prop={'size':12})
plt.xlabel("x")
plt.ylabel("Legendre")
plt.show()

			
