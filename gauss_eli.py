import numpy as np

def GaussElimn(a,b):
    n=len(b)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if(a[i,k] != 0.0):
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]


    for k in range(n-1,-1,-1):
        b[k]=(b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

m = int(input("Input the number of equations = "))
n = int(input("Input the number of variables = "))

if m==n:
	A = np.array([[0 for j in range(n)] for i in range(0,m)])
	B = np.array([0 for i in range(m)])
	for i in range(0,m):
		for j in range(0,n):
			A[i,j] = float(input("Input a[%s][%s] = "%(i,j)))
	for i in range(n):
		print("\n",A[i])
	print("Give the constants of each equation:\n")

	for i in range(0,n):
		B[i] = float(input("Input b[%s] = "%(i)))
	sols = GaussElimn(A,B)
	print("Solutions are : \n")
	for i in range(n):
		print("X[%s] = "%(i+1), sols[i])

else:
	print("Dabi ta ke re tor?, row column soman deta paris na?")