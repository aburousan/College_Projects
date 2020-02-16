import numpy as np

m = int(input("Input the number of rows = "))
n = int(input("Input the number of columns = "))


def Gauss_Jordon(A):
	n = len(A)
	if n==len(A[0]):
		B = np.identity(n)
		for i in range(n):
			for j in range(n):
				if j!=i:
					l = A[j][i]/A[i][i]
					for k in range(n):
						A[j][k] = 	A[j][k] - l*A[i][k]
						B[j][k] = 	B[j][k] - l*B[i][k]
		for i in range(n):
			for j in range(n):
				B[i][j] = 	B[i][j]/A[i][i]
	return B


A = np.array([[0 for j in range(n)] for i in range(m)])
if n == m:
	for i in range(0,m):
		for j in range(0,n):
			A[i][j] = float(input("Input A[%s][%s] = "%(i,j)))
	for i in range(n):
		print("\n",A[i])
	inverse_A = Gauss_Jordon(A)
	print("Inverse of The matrix is : \n")
	for i in range(n):
		print("\n",inverse_A[i])


else:
	print("Error! Wara Poris ne --j Gauss-Jordon a unit matrix lagha?")