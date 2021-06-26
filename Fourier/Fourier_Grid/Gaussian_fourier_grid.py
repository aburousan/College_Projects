import numpy as np
from scipy.linalg import eigh
from scipy.integrate import simps

def H_matrix(L, V, mass=1):
	N = len(V)
	print("Value of N = ",N)

	print("Value of  mass = ",mass)
	Hij = np.zeros([N,N])
	n = int(N/2); dk = (2*np.pi)/(L)
	T0 = (dk**2)/(2*mass)

	for i in range(N):
		for j in range(i+1):
			if i == j:
				Hij[i,j] = (T0*n*(n-1)*(2*n-1))/(3*N)+(T0*n**2)/N+ V[i]
			else:
				s = 0
				for l in range(1,n):
					s += (l**2)*np.cos((l*2*np.pi*(i-j))/N)
				Hij[i,j] = ((2*s*T0)+(((-1)**(i-j))*T0*n**2))/N
				Hij[j, i] = Hij[i, j]  # use Hermitian symmetry
				
	return Hij

def v(x,a=1,V0=1):
	d = -V0*np.exp(-a*x**2)
	return d


L = 20
N = 130
dx = L/N

R_min = -10 ; R_max = 10
x = np.linspace(R_min,R_max,N,endpoint=False)

V = v(x)
H = H_matrix(L,V,1)

Eig_val,Eig_vec = eigh(H)
print(Eig_val)
