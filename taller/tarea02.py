import numpy as np
import matplotlib.pyplot as plt


"""
[[a, b], *[x,y] = [e,f]
 [c, d]]
"""
def resolverSist(a,b,c,d,e,f):
    if a != 0:
        try:
            y = (f - (c/a)*e)/(d - (c/a)*b)
            x = ( e - b*y) / a
            print("16bits: x =" + str(x) +" , y =" + str(y))
        except Exception as err:
            print("Error:" + str(err)) 
    else:
        print("a es cero o indefinida")

#1.A
"""
resolverSist(np.float16(1.130),
             np.float16(6.990),
             np.float16(1.013),
             np.float16(6.099),
             np.float16(14.20),
             np.float16(4.22))
"""
#1.B



#polinomino de la forma dX^3  + ex^2 + f = 0 

e = 0.075 - (1.2**2 + 2*0.6**3*9.81*1.8**2)/(2*9.81*1.8**2*0.6**2)
f = (1.2**2)/(2*9.81*1.8**2)


def func(h):
    value  = h**3 + e*h**2 +f
    return value

def funcDerivada(h):
    value = 3*h**2 + 2*e*h 
    return value

"""
xValue = []
yValue = []

for i in range(-5000,6000):
    yValue.append(func(i*10**-4))
    xValue.append(i*10**-4)


plt.figure()
ax = plt.axes()
ax.plot(xValue, yValue, '.-')
ax.grid()
plt.show()
"""

"""
Avaluar en los intervalos
[-0.4,-0.1]
[-0.1, 0.4]
[0.3, 0.5]
"""

x1 = -0.15
x2 = 0.3

Tol = 1.0e-4
error = 1.0
Nmax = 1000
iteracion = 0

def sign(x):
  if x > 0:
    return 1
  elif x < 0:
    return -1
  else: 
    return 0


#Metodo bisección 
"""
if (sign(func(x1))* sign(func(x2))<0):
    while(error > Tol): 
        pi = 0.5*(x1+x2)
        pi_previo = pi

        #redefinimos los limites del intervalo
        #if(abs(func(pi)) < Tol):
        # print("La raiz del polinomio es %.5f"%(pi))
        #else:
        if(sign(func(pi)) == sign(func(x1))):
            x1 = pi
            x2 = x2
        elif(sign(func(pi)) == sign(func(x2))):
            x1 = x1
            x2 = pi

        pi = 0.5*(x1+x2)
        error = abs(pi - pi_previo)
        iteracion += 1
    
        print("pi=%f\t x1=%f\t f(pi)=% f\t error=%f"%(pi,x1,func(pi),error))

        if(iteracion > Nmax):
            print("Numero de iteraciones excedido")
            break
    else:
        print("Intervalo inadecuado")

print("Cero de F(x)  = %f , F(pi)= %f, error= %f"%(pi, func(pi), error))
"""
#Motodo Newton-Raphson
"""
xpre =  -0.1
xcurt = 0
while(error > Tol):
    #xcurt = xpre - func(xpre)/funcDerivada(xpre)
    xcurt = xpre - func(xpre)/funcDerivada(xpre)
    error = abs(xpre - xcurt)
    iteracion += 1
    
    print("xpre=%f\t xcurt=%f\t f(xcurt)=% f\t error=%f"%(xpre,xcurt,func(xcurt),error))
    xpre = xcurt
    if(iteracion > Nmax):
        print("Numero de iteraciones  exepdido")
        break
"""
"""
EL metodo de newton-raphson es mas preciso y eficiente, en comparación con el metodo de
Bisección. En ambos casos es  necesario tener una idea del comportamiento de la función,
el metodo de newton presenta problemas con puntos muy cercanos a maximos o minimos y  el metodo de 
bisección por la limitante de la maquina falla  cuando el intervalo es pequeño  o hay un  extremo del 
intervalo muy cercano al punto cero
"""

#3
#z^2 + 62.10z +1 = 0
# a = 1, b = 62.10 , c = 1

z1 = np.float16((-62.10 + (62.10**2 - 4)**0.5)/2)
z1r = np.float16(-2/(62.10 + (62.10**2 - 4)**0.5))

z2 = np.float16((-62.10 - (62.10**2 - 4)**0.5)/2)
z2r = np.float16(-2/(62.10 - (62.10**2 - 4)**0.5))

print("z1=%f\t z1r=%f\t z2=% f\t z2r=%f"%(z1,z1r,z2,z2r))

"""
El resultado fue el mismo, sin embargo sse debe notar que cuando usamos la forma 
de z1 si 4ac en   la raiz es muy pequeño entonces  el resultado de la raiz de la formula
seria (b^2)^(1/2) = b, que daria cero al aplicar (-b + b) = 0 dando un valor erroneo 
laa forma de z1r nos asegura una mejor aproximación 
"""