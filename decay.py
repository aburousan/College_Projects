import numpy as np
import matplotlib.pyplot as plt


def Euler(fun,x0,y0,dx,X):
	x_val = []; y_val = []; dydx_val = []
	while abs(x0)<abs(X):
		dydx = fun(y0)
		x_val.append(x0); y_val.append(y0)
		dydx_val.append(dydx)
		y0 = y0 + dydx*dx
		x0 = x0 + dx
	return x_val,y_val,dydx_val

def fun(N):
	return 0.6*N

x0, y0 = [float(d) for d in input("Give me boundary Values(eg: t N(t)) = ").split()]
X1 = float(input("Give me maximum value of time(t) = "))
dx = float(input("Give me value of dt = "))
X = np.arange(0.0,25.0,0.01)
plt.plot(X,np.exp(0.6*X),c='red',label='Exact Solution')
t,N,dydx = Euler(fun,x0,y0,dx,X1)

for i in range(len(t)):
	print("(t(%s),N(%s)) ="%(i,t[i]),N[i])

tt = "dx = %.4f "%(dx)
plt.plot(t,N,c='blue',ls='--',label=tt)
plt.title("Radioactive decay eqn plot")
plt.legend(loc='best',prop={'size':12})
plt.xlabel("time")
plt.ylabel("Particle No.")
plt.savefig('Decay.pdf')
plt.show()
