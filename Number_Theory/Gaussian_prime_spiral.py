import numpy as np
import matplotlib.pyplot as plt
from sympy import isprime#use this to check if a number is ordinary prime or not

def gprime(z):#check if z is gaussian prime or not, return true or false
	re = int(abs(z.real)); im = int(abs(z.imag))
	if re == 0 and im == 0:
		return False
	d = (re**2+im**2) 
	if re != 0 and im != 0:
		return isprime(d)
	if re == 0 or im == 0:
		abs_val = int(abs(z))
		if abs_val % 4 == 3:
			return isprime(abs_val)
		else:
			return False

def gaussian_spiral(seed, loop_num = 1, del_c = 1, initial_con = True):#Initial condition is actually the fact
#that represnet if you want to get back to the initial number(seed) at the end.
	d = seed; points = np.array([seed]); gaussian_primes = np.array([])#Seed is the initial point; points hold all generated gaussian integers
	if initial_con:
		while True:
			seed += del_c
			points = np.append(points,seed)
			if seed == d:
				break
			if gprime(seed):
				del_c *= 1j ; gaussian_primes = np.append(gaussian_primes,seed)
	else:
		for i in range(loop_num):
			seed += del_c
			points = np.append(points,seed)
			if gprime(seed):
				del_c *= 1j ; gaussian_primes = np.append(gaussian_primes,seed)
	points_x = points.real; points_y = points.imag; gauss_primes = np.array([gaussian_primes.real,gaussian_primes.imag])
	return points_x, points_y, gauss_primes

seed1 = 5 + 23*1j #first plot
plot_x, plot_y, primes= gaussian_spiral(seed1)
loop_no = len(plot_x)-1
plt.ylim(21,96.5)
plt.xlim(-35,35)
plt.axhline(0,color='Black');plt.axvline(0,color='Black')
plt.plot(plot_x,plot_y,label='Gaussian spiral',color='mediumblue')
plt.scatter(primes[0][0],primes[1][0],c='Black',marker='X')#starting point
plt.scatter(primes[0][1::],primes[1][1::],c='Red',marker='*',label='Gaussian primes')
plt.grid(color='purple',linestyle='--')
plt.legend(loc='best',prop={'size':6})
plt.xlabel("Re(z) ; starting point = %s and loop number = %s "%(seed1,loop_no))
plt.ylabel("Im(z)")
# plt.title("Gaussian Primes spiral")
plt.savefig("img1_new.pdf", bbox_inches = 'tight',dpi = 300)
#___________________________________________________________________________________________________________-
# seed2 = 60 + 1j
# plot_x, plot_y, primes= gaussian_spiral(seed2)
# loop_no = len(plot_x)-1
# plt.ylim(-271,271)
# plt.xlim(-194,194)
# plt.axhline(0,color='Black');plt.axvline(0,color='Black')
# plt.plot(plot_x,plot_y,label='Gaussian spiral',color='mediumblue')
# plt.scatter(primes[0][0],primes[1][0],c='Black',marker='X')#starting point
# plt.scatter(primes[0][1::],primes[1][1::],c='Red',marker='*',label='Gaussian primes')
# plt.grid(color='purple',linestyle='--')
# plt.legend(loc='best',prop={'size':6})
# plt.xlabel("Re(z); starting point = %s and loop number = %s "%(seed2,loop_no))
# plt.ylabel("Im(z)")
# # plt.title("Gaussian Primes spiral")
# # plt.show()
# plt.savefig("img4_new.pdf", bbox_inches = 'tight',dpi = 300)
#_________________________________________________________________________________________-
#seed3 = 277 + 232*1j # This one can kill your computer. Try at your own risk!!
# plot_x, plot_y, primes= gaussian_spiral(seed3)
# loop_no = len(plot_x)-1
# plt.ylim(-4000,4000)
# plt.xlim(-4000,4000)
# plt.axhline(0,color='Black');plt.axvline(0,color='Black')
# plt.plot(plot_x,plot_y,label='Gaussian spiral',color='mediumblue',bbox_inches = 'tight')
# plt.scatter(primes[0][0],primes[1][0],c='Black',marker='X')#starting point
# plt.scatter(primes[0][1::],primes[1][1::],c='Red',marker='*',label='Gaussian primes',s=0.0001)
# plt.grid(color='purple',linestyle='--')
# plt.legend(loc='best',prop={'size':6})
# plt.xlabel("Re(z); starting point = %s and loop number = %s "%(seed3,loop_no))
# plt.ylabel("Im(z)")
# # plt.title("Gaussian Primes spiral")
# plt.show()
#_____________________________________________________________________________
# seed4 = 3 + 2*1j
# plot_x, plot_y, primes = gaussian_spiral(seed4,loop_num=30, initial_con = False)
# loop_no = len(plot_x)-1
# plt.ylim(1.5,8.5)
# # plt.xlim(-194,194)
# plt.axhline(0,color='Black');plt.axvline(0,color='Black')
# plt.plot(plot_x,plot_y,label='Gaussian spiral',color='mediumblue')
# plt.scatter(plot_x,plot_y,c='Black',marker='o',label='Gaussian Integers')
# plt.scatter(primes[0][0],primes[1][0],c='Black',marker='X')#starting point
# plt.scatter(primes[0][1::],primes[1][1::],c='Red',marker='*',label='Gaussian primes')
# plt.grid(color='purple',linestyle='--')
# plt.legend(loc='best',prop={'size':6})
# plt.xlabel("Re(z); starting point = %s and loop number = %s "%(seed4,loop_no))
# plt.ylabel("Im(z)")
# # plt.title("Gaussian Primes spiral")
# # plt.show()
# plt.savefig("img3_new.pdf", bbox_inches = 'tight',dpi = 300)
