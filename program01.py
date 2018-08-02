import numpy as np
import  matplotlib.pyplot as plt

def factorial(n):
    if n == 0:
        return 1
    else:
        fat = 1
        for i in range(1, n+1):
            fat = fat *i
        
        return  fat 
        

print(factorial(5))


def cos(x,n):
    resul  = 0
    for i in range(0,n+1):
        resul += (-1)**i * x**(2*i)/factorial(2*i)
    return resul

"""
x = int(raw_input("The value of x:"))
n = int(raw_input("The value of n:"))
print(cos(x,n))
"""

Npoints = 100
dtheta = (2.0*np.pi -0.0)/Npoints
Nterm = 10

theta = []
ctheta = []

for i in range(0, Npoints):
    theta.append(i*dtheta)
    ctheta.append(cos(i*dtheta, Nterm ))

fig = plt.figure()
ax= plt.axes()
ax.plot(theta,ctheta, '.')
ax.plot(theta,np.cos(theta))
ax.grid()
ax.set_xlabel(r"$\theta$", fontsize=14)
plt.show()
plt.savefig('cos.png')


