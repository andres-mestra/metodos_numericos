import numpy as np
import matplotlib.pyplot as plt  
"""
Y = ((Y_(i+1) - Y_i)/(X_(i+1) - X_i))*(X - X_i) +Y_i

Programación

1. Cargar dato:
X = []
Y = []

2. Def Interpolación Lineal: (X[],Y[]):
for(i=0, len(X[])-1):
    if(x >= xi and x =< X_(i+1) ):
        calcule m, b, y
        return y
"""

datos = np.loadtxt("datos.dat")
x_list = []
y_list = []

for i in range(0,datos.shape[0]):
    x_list.append(datos[i][0])
    y_list.append(datos[i][1])


def intPLineal(x_list, y_list,x):
    for i in range(0, len(x_list)):
        if(x >= x_list[i] and x <= x_list[i+1]):
            x_prev = x_list[i] #X_i
            y_prev  = y_list[i] #  Y_i
            x_next = x_list[i+1] #X_i+1
            y_next = y_list[i+1]#Y_i+1

            y = (y_next - y_prev)/(x_next - x_prev)*(x - x_prev) + y_prev
            return y 
    
x_interpol = np.linspace(min(x_list), max(x_list),100)
y_interpol = []

for i in range(0,len(x_interpol)):
    y_interpol.append(intPLineal(x_list,y_list,x_interpol[i]))

fig = plt.figure()
ax = plt.axes()
ax.plot(x_list, y_list,'*',markersize='10', label='Datos Discretos')
ax.plot(x_interpol, y_interpol,'.', label='Puntos interpolados')
ax.plot(x_interpol, np.sin(x_interpol), label='sin(x)')
ax.legend()
plt.show()
#print(intPLineal(x_list,y_list,0.5))


