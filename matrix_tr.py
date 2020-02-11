import numpy as np

m = int(input("Input the number of rows  = "))
n = int(input("Input the number of colomn ="))

a = [[0 for j in range(n)] for i in range(0,m)]

for i in range(0,m):
	for j in range(0,n):
		a[i][j] = float(input("Input a[%s][%s] = "%(i,j)))

trace = 0
if m==n:
	for i in range(n):
	    trace = trace + a[i][i]
else:
	print("Trace is not possiblr.Amake cos2 dis na!!")
print("Matrix = ")
for i in range(n):
	print("\n",a[i])


print("Trace = ",trace)


