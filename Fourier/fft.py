import matplotlib.pyplot as plt
import numpy as np

N = 1000#No of sample points
T = 100#Time period
sigma = 1 ;t0=50
t_set = np.linspace(0,T,N)
#__________________________________
def func(t,t0=50,sigma=1):
	y = np.exp(-abs((t-t0)**2)/(2*sigma**2))
	#y = np.sin(an_vel*t*2)+np.cos((3*t-t0)*an_vel)
	return y

plot, dif = plt.subplots(2,1)#Represent 1 row, 2 column
#__________________________________
func_val = func(t_set)
dif[0].plot(t_set,func_val,c='red',label='Sigma=%s and t0=%d'%(sigma,t0))
dif[0].legend(loc='best')
dif[0].set_title(r'Gaussian Function')
dif[0].set_xlabel('Time'); dif[0].set_ylabel('Function')
#_______________________________________________________
fre_set = np.fft.fftfreq(N)#All the frequency for fourier transform horizontal axis
mask = fre_set>0
fft_val = 2*np.abs(np.fft.fft(func_val))
fft_nor = (fft_val)/max(fft_val)

dif[1].plot(fre_set[mask],fft_nor[mask],c='green')
#dif[1].plot(fre_set,fft_nor,c='green')
#In quantum domain we work with negative frequency so for that just remove mask i.e., and line 29 and comment in line 30
dif[1].set_title('Fast Fourier Transform')
dif[1].set_xlabel('Frequency'); dif[1].set_ylabel('Transform G')
plt.show()
