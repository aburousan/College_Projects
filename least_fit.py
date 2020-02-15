import numpy as np
import matplotlib.pyplot as plt

def tangent(V,I):
	n = len(V)
	if n != len(I):
		print("Input and Output are not matching. Dabi thik kor")
	else:
		sumVI=0; sum2=0
		for i in range(n):
			sumVI = sumVI + V[i]*I[i]
			sum2 = sum2 + I[i]*I[i]
		return sumVI/sum2

V = []; I = []
t = int(input("Give me number of datas = "))
for i in range(t):
	j = i+1
	x, y = [float(d) for d in input("Enter I-V values(Eg: 3 2) = ").split()]
	I.append(x); V.append(y)
m = tangent(V,I)#V = I R
def lin(x):
	return m*x
I_ex = np.arange(0,I[len(I)-1],0.001)
V_ex = lin(I_ex)
plt.plot(I_ex,V_ex,label=r'least_sqr_fit')
plt.plot(I,V,"red",ls=" ",marker='.',label=r'Ex-value')
plt.legend(loc='best',prop={'size':12})
plt.xlabel('Current')
plt.ylabel('Voltage')
plt.title('Least Square Fit for Y=MX type')
plt.show()