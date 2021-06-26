import numpy as np
from scipy.linalg import eigh
from scipy.integrate import simps

def H_matrix(L, V, mass):
	N = len(V)
	print("Value of N = ",N)

	print("Value of reduced mass = ",mass)
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

def v(x,x0=1.7329,D=0.2250073497,a = 1.1741):
	d = D*(1-np.exp(-a*(x-x0)))**2
	return d


L = 4.85212000000000021
N = 128
dx = L/N

R0 = 1.7329; R_min = R0*0.2 ; R_max = R0*3
x = np.linspace(R_min,R_max,N,endpoint=False)

V = v(x)
H = H_matrix(L,V,1836.9822)

Eig_val,Eig_vec = eigh(H)
print(Eig_val)
