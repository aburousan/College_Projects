import matplotlib.pyplot as plt
import numpy as np

def fourier_triangle(t,n):
    summ = 0
    for i in range(n):
        s = 2*i + 1
        summ = summ + (np.sin(t*s)*(pow(-1,(s-1)/2)))/(s*s)
    return summ*(8/(np.pi)**2)


color = ['red','blue','green','black']
t = np.linspace(-np.pi, np.pi, 400)

for i in range(1,5):
    plt.plot(t,fourier_triangle(t,np.math.factorial(i)),c=color[i-1],label='No. of terms = %s'%(np.math.factorial(i)))
plt.legend(loc='best',prop={'size':12})
plt.title('Triangular wave')
plt.grid()
plt.show()