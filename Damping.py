import matplotlib.pyplot as plt


def runge_kutta(f,t0,x0,dt,dxdt_0,t_max,b,w):
	T = []; X = []
	a = [0,0.5,0.5,1];k = [[0 for j in range(4)] for i in range(2)];
	while abs(t0)<abs(t_max):
		k[0][0]=dt*dxdt_0; g = k[0][0]; k[1][0]=dt*f(t0,x0,dxdt_0,b,w); c = k[1][0]
		for j in range(1,4):
			k[0][j] = dt*(dxdt_0 +(c*a[j]))
			k[1][j] = dt*f(t0+(a[j]*dt),x0+(a[j]*g),dxdt_0+(a[j]*c),b,w)
			g = k[0][j]; c = k[1][j]
		dx = (1/6)*(k[0][0]+ 2*k[0][1]+ 2*k[0][2]+k[0][3])
		dx2 = (1/6)*(k[1][0]+ 2*k[1][1]+ 2*k[1][2]+k[1][3])
		X.append(x0); T.append(t0)
		t0 = t0 + dt ; x0 = x0 + dx; dxdt_0 = dxdt_0 + dx2
	return T , X



def f(t,x,dxdt,b,w):
	return -((2*b*dxdt)+(w*w*x))

dt = 0.001
b=float(input("The value of damping constane  = "))
w=float(input("The value of natural frequency = "))

t0, x0 = [float(d) for d in input("Give me boundary Values(eg: t x(t)) = ").split()]
dxdt_0 = float(input("The value of initial velocity  = "))
t_max=float(input("Give the Final Time = "))

sol_T, sol_X = runge_kutta(f,t0,x0,dt,dxdt_0,t_max,b,w)

plt.plot(sol_T,sol_X,c='red',label='b = %s ;w = %s \n t0 = %s ; x0 = %s ; v0 = %s'%(b,w,t0,x0,dxdt_0))
plt.legend(loc='best',prop={'size':12})
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.title(" damping curve")
plt.show()
