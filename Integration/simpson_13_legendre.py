#by K.A.Rousan
n = float(input("Give the value of n = "))
m = float(input("Give the value of m = "))
def p(n,x):
    if (n==0):
        return 1
    if (n==1):
        return x
    else:
        return (((2*n)-1)*x*p(n-1,x)-(n-1)*p(n-2,x))/n

def p_p(x):
    global n; global m
    return p(n,x)*p(m,x)

def simpson1_3(fun,a,b,n=100,tol=0.0000001):
    number_of_cuts = n; I_1 = 0
    while True:
        h = (b-a)/number_of_cuts
        I_2 = 0
        for i in range(number_of_cuts+1):
            if i == 0 or i == n:
                I_2 += fun(a+i*h)
            if i%2 == 0:
                I_2 += 2*fun(a+i*h)
            else:
                I_2 += 4*fun(a+i*h)
        I_2 *= h/3
        if abs(I_2-I_1)<= tol:
            break
        else:
            I_1 = I_2
            number_of_cuts += 10
    return I_2

def delta(n,m):
    if n == m:
        return 1
    else:
        return 0

integration_val = simpson1_3(p_p,-1,1)
right_side = delta(n,m)*(2/(2*n+1))
print("Integration value = ",integration_val)
print("Right Side  value = ",right_side)
if abs(integration_val - right_side)<=0.001:
    print("The equation is satisfied.")
    print("There is a little error due to simpson 1/3, It can be removed by decreasing tol parameter.")
else:
    print("The equation is not satisfied.")
