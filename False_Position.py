#False Position Method

import math

x0 = float(input("Enter x0"))
x1 = float(input("Enter x1"))
N = int(input("Enter number of Iterations"))
err = float(input("Enter permissible error"))

def f(x):
    return 5*math.pow(math.sin(x), 2) - 8*math.pow(math.cos(x), 5) 

def f1(x):
    return math.pow(x, 2) - 2*x - 1

def find_roots(x0, x1, N, err):
    for i in range(1,N+1):
        x2 = (f(x1)*x0 - f(x0)*x1) / (f(x1) - f(x0)) # using f1 for x^2-2x-1
        print (" Root at iteration ",i," is :", x2)
        if abs((x2 - x1)/x1) < err:
             print("Root is:", x2)
             break
        if f(x1)*f(x2) < 0:
            x1, x0 = x2, x1
        else :
            x1 = x2
    print (f(x2))

find_roots(x0, x1, N, err) 
 
print ('Done')
