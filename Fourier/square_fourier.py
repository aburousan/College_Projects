import matplotlib.pyplot as plt
import numpy as np

def fourier_square(t,n):
    summ = 0
    for i in range(n):
        s = 2*i + 1
        summ = summ + ((np.sin(t*s))/s)
    return summ*(4/np.pi)


color = ['red','blue','yellow','green','black']
t = np.linspace(-np.pi, np.pi, 400)

for i in range(1,6):
    plt.plot(t,fourier_square(t,np.math.factorial(i)),c=color[i-1],label='No. of terms = %s'%(np.math.factorial(i)))
plt.legend(loc='best',prop={'size':12})
plt.title('Square wave')
plt.grid()
plt.show()