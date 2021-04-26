import numpy as np
import matplotlib.pyplot as plt
from sympy import isprime#use this to check if a number is ordinary prime or not

def gprime(z):#check if z is gaussian prime or not, return true or false
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
d = seed[0]+1j*seed[1]; d0=d; s = 1
plot_x = [seed[0]]; plot_y = [seed[1]]; primes = [[d.real],[d.imag]]
while True:#Replace this line by for i in range(100): for 100 steps
# for i in range(1000):
	d = direct + d; s+=1
	plot_x.append(int(d.real)); plot_y.append(int(d.imag))
	if (seed[0]+1j*seed[1])==d:#if you use for i in range, then delete this
	#if statement and break
		break
	if gprime(d):
		direct = direct*1j
		primes[0].append(d.real);primes[1].append(d.imag)


plt.axhline(0,color='Black');plt.axvline(0,color='Black')
plt.plot(plot_x,plot_y,label='Gaussian spiral',color='mediumblue',linewidth=0.1)
# plt.scatter(plot_x,plot_y,c='Black',label='Gaussian integers')
plt.scatter(primes[0][0],primes[1][0],c='Black',marker='X')#starting point
plt.scatter(primes[0][1::],primes[1][1::],c='Red',marker='*',label='Gaussian primes')#,s=0.0001)
plt.grid(color='purple',linestyle='--')
plt.legend(loc='best',prop={'size':6})
plt.xlabel("x ; starting point = %s and loop number = %s "%(d0,s))
plt.ylabel("y")
# plt.title("Gaussian Primes spiral")
plt.show()
