import numpy as np
import matplotlib.pyplot as plt
#Cancelacion sustractiva
a = 1.0
b = 1.0
x_list = []
y_list = []

for  i in range(1,10):
    c=10**(-i)
    x_1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    x_1_p = 2*c/(-b-(b**2-4*a*c)**0.5)
    error = abs(x_1_p - x_1)/abs(x_1_p)*100.0
    x_list.append(c)
    y_list.append(error)
    #print("c = %.16e x_1=%.5e x_1_p=%.16e error=%.16f"%(c,x_1,x_1_p,error))

fig=plt.figure(figsize=(6,6))
ax = plt.axes()
ax.plot(x_list, y_list,'.',markersize=10)
ax.grid()
ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlabel("C")
ax.set_ylabel("Error")
plt.show()




