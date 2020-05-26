import matplotlib.pyplot as plt
import numpy as np

def fourier(t,f,coff,n):
    sum = 0
    for i in range(1,n+2):
        sum = sum + coff(i)*f(t,i)
    return sum

def f(t,i):#For square and triangular same
    return np.sin(i*t)
def coff_squ(i):
    return (2/(np.pi*i))*(1-pow(-1,i))
def coff_triangle(i):
    if i%2==0:
        s = 0
    else:
        s = (8/(np.pi*i)**2)*(pow(-1,(i-1)/2))
    return s


color = ['red','blue','yellow','green','black']
t = np.linspace(-np.pi, np.pi, 400)
plt.suptitle('Wave approximation using Fourier')
plt.subplot(2,1,1)
for i in range(1,6):
    plt.plot(t, fourier(t,f,coff_squ,np.math.factorial(i)),c=color[i-1],label='No of terms = %s'%(np.math.factorial(i)))
plt.legend(loc='best',prop={'size':12})
plt.grid()
plt.ylabel('Square Wave')

plt.subplot(2,1,2)
for i in range(1,6):
    plt.plot(t, fourier(t,f,coff_triangle,np.math.factorial(i)),c=color[i-1],label='No of terms = %s'%(np.math.factorial(i)))
plt.legend(loc='best',prop={'size':12})
plt.ylabel('Triangle Wave')
plt.grid()
plt.show()
