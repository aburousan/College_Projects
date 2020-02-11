import numpy as np
#For linear
def least_fig(a,b):
	nb=len(b)
	x_sum=np.sum(a)
	y_sum = np.sum(b)
	xy_sum=0
	x_2=0
	for i in range(nb):
		xy_sum=xy_sum+a[i]*b[i]
	for j in range(nb):
		x_2 = x_2+pow(a[j],2)
	A=np.array([[x_sum,nb],[x_2,x_sum]])
	B = np.array([y_sum,xy_sum])
	solution = np.linalg.solve(A,B)
	#print("The least matrix is=",A,B)
	print("m = ",solution[0])
	print("c =  ",solution[1])
	equation = print("y=(",solution[0],")x+(",solution[1],")")
#End

#For parabolic
def least_fit_para(a,b):
	nb=len(b)
	x_sum=np.sum(a)
	y_sum = np.sum(b)
	xy_sum=0
	x_2=0
	x2y_sum=0
	x_3=0
	x_4=0
	for i in range(nb):#For xy
		xy_sum=xy_sum+a[i]*b[i]
	for j in range(nb):#For x^2
		x_2 = x_2+pow(a[j],2)
	for j in range(nb):#for x^2y
		x2y_sum=x2y_sum+pow(a[j],2)*b[j]
	for j in range(nb):#for x^2
		x_3=x_3+pow(a[j],3)
	for j in range(nb):#for x^4
		x_4=x_4+pow(a[j],4)
	A=np.array([[nb,x_sum,x_2],[x_sum,x_2,x_3],[x_2,x_3,x_4]])
	B = np.array([y_sum,xy_sum,x2y_sum])
	solution = np.linalg.solve(A,B)
	print("a = ",solution[0])
	print("b =  ",solution[1])
	print("c = ",solution[2])
	equation = print("y=(",solution[0],")x+(",solution[1],")x+(",solution[2],")x^2")
#End

ax = []
by = []
m=int(input("Enter the number of reading = "))
print("Give me values of x and y(eg: 1 2)")
for i in range(m):
	x,y= map(int, input("(x,y)=").split())
	ax.append(x)
	by.append(y)

choose=int(input("Choose Linear(0) or parabolic(1) = "))
if choose==0:
	Ww = least_fig(ax,by)
elif choose==1:
	Ww = least_fit_para(ax,by)
else:
	print("Invalid syntax--Tor dabi ta ke--Input 0 or 1 only")
