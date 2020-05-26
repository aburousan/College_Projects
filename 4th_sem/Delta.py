import matplotlib.pyplot as plt
import numpy as np

def func(x,sigma):
	return np.exp(-((2-x)**2)/(2*sigma**2))*(x+3)

def trapizoid(f,a,b,sigma):
	n = 20000; fa = f(a,sigma); fb = f(b,sigma);
	h = (b-a)/n; I_mid = 0
	for i in range(1,n):
		I_mid = I_mid + f(a+i*h,sigma)
	I = h/2*(fa+fb+2*I_mid)
	norm = 1/np.sqrt(2*np.pi*sigma**2)
	return norm*I

val = [0.001,0.01,0.1,1,10]
for i in val:
	f = trapizoid(func,1,3,i)
	print('Value of Integration for sigma = %s is = '%(i),f)

#___________________________________________________
#This shows for the approching part
sigma_value = np.linspace(0.001,10,10000);
f = trapizoid(func,1,3,sigma_value)
plt.plot(sigma_value,f,c='red',ls='--',label=r'$\delta$ as func of $\sigma$')
plt.title('Dirac Delta Function')
plt.legend(loc='best',prop={'size':12})
plt.xlabel(r'value of $\sigma$')
plt.ylabel(r'value of Integration')
plt.grid()
plt.show()
