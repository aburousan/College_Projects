import matplotlib.pyplot as plt
import numpy as np

N = 100#No of sample points
T = 1/N#Sampling Interval
sigma = 0.5 ;t0=2
begin_t = 0; end_t = 10;
t_set = np.linspace(begin_t,end_t,N)
#__________________________________
def func(t,t0=2,sigma=0.5):
	return np.exp(-abs((t-t0)**2)/(2*sigma**2))

plot, dif = plt.subplots(2,1)#Represent 1 row, 2 column
#__________________________________
dif[0].plot(t_set,func(t_set),c='red',label='Sigma=%s and t0=%d'%(sigma,t0))
dif[0].legend(loc='best')
dif[0].set_title(r'Gaussian Function')
dif[0].set_xlabel('Time'); dif[0].set_ylabel('Function')
#_______________________________________________________
ff_t = np.fft.fftshift(func(t_set))/len(t_set)#Normalize
f_count = len(ff_t)
time_period = f_count/N
f_se = np.linspace(0,end_t,N)
f_set = f_se/time_period

dif[1].plot(f_set,abs(ff_t),c='green')
dif[1].set_title('Fast Fourier Transform')
dif[1].set_xlabel('Frequency'); dif[1].set_ylabel('Transform G')
plt.show()
