import numpy as np 

def factorial(n):
    if n == 0:
        print 1
    else:
        fat = 1
        for i in range(1, n+1):
            fat = fat *i
        
        return  fat 
        

print(factorial(3))

def cos(x,n):
    resul  = 0
    for i in range(0,n+1):
        resul += (-1**i)*x**(2*i+1)/factorial(2*i+1)
    return resul

x = int(raw_input("The value of x:"))
n = int(raw_input("The value of n:"))
print(cos(x,n))

