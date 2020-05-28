import matplotlib.pyplot as plt
import numpy as np
import wave


audio_file = wave.open("music.wav","r")
signal = audio_file.readframes(-1)
signal = np.fromstring(signal,"Int16")
f_rate = audio_file.getframerate()#No of variation per secnd
#____________________________________

N = len(signal)#No of sample points
T = len(signal)/f_rate
t_set = np.linspace(0,T,N)

plot, dif = plt.subplots(2,1)#Represent 1 row, 2 column
#__________________________________
func_val = signal
dif[0].plot(t_set,func_val,c='red')
dif[0].set_title(r'Audio Signal')
dif[0].set_xlabel('Time'); dif[0].set_ylabel('Audio Amplitude')
#_______________________________________________________
fre_set = np.fft.fftfreq(N)#All the frequency for fourier transform horizontal axis
mask = fre_set>0
fft_vals = 2*np.abs(np.fft.fft(func_val)/len(fre_set))

dif[1].plot(fre_set[mask],fft_vals[mask],c='green')
#dif[1].plot(fre_set,fft_vals,c='green')
#In quantum domain we work with negative frequency so for that just remove mask i.e., and line 29 and comment in line 30
dif[1].set_title('Fast Fourier Transform')
dif[1].set_xlabel('Frequency'); dif[1].set_ylabel('Transform Amplitude(Normalized)')
plt.show()
