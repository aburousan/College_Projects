import numpy as np
import matplotlib.pyplot as plt
from sympy import isprime


def gprime(z):#check if z is gaussian prime or not, return true or false based upon it
	re = int(abs(z.real)); im = int(abs(z.imag))
	if re==0 and isprime(im)==True:
		if im % 4 == 3:
			return True
		else:
			return False
	if im == 0 and isprime(re)==True:
		if re % 4 == 3:
			return True
		else:
			return False
	d = (re**2+im**2)
	if isprime(d):
		return True
	else:
		return False

seed = [-2,11]#Initial point
direct = 1# direction of increment
d = seed[0]+1j*seed[1]; d0=d
plot_x = [seed[0]]; plot_y = [seed[1]]; primes = [[d.real],[d.imag]]
while True:
	d = direct + d
	plot_x.append(int(d.real)); plot_y.append(int(d.imag))
	if (seed[0]+1j*seed[1])==d:
		break
	if gprime(d):
		direct = direct*1j
		primes[0].append(d.real);primes[1].append(d.imag)


#x1 = np.ma.masked_array(plot_x[:-1], np.diff(plot_x)>=0)
#x2 = np.ma.masked_array(plot_x[:-1], np.diff(plot_x)<=0)


plt.axhline(0,color='Black');plt.axvline(0,color='Black')
plt.plot(plot_x,plot_y,label='Gaussian spiral',color='mediumblue')
# plt.plot(x1, plot_y[:-1],'k<',linewidth=1,markevery=20)
# plt.plot(x2, plot_y[:-1],'k>',linewidth=1,markevery=20)
plt.scatter(primes[0][0],primes[1][0],c='Black',marker='X')
plt.scatter(primes[0][1::],primes[1][1::],c='Red',marker='*',label='Gaussian primes')
plt.grid(color='purple',linestyle='--')
plt.legend(loc='best',prop={'size':6})
plt.xlabel("x ; starting point = %s"%d0)
plt.ylabel("y")
plt.title("Gaussian Integers and Primes spiral")
plt.show()
