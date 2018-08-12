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

"""
xValue = []
yValue = []

for i in range(-5000,6000):
    yValue.append(func(i*10**-4))
    xValue.append(i*10**-4)
    print(i*10**-4)


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
[0.35, 0.55]
"""

x1 = 0.35
x2 = 0.55

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
        print("Error = %.5e"%(error))
        iteracion = iteracion+1
    
        print("pi=%f\t x1=%f\t f(pi)=% f\t error=%f"%(pi,x1,func(pi),error))

        if(iteracion > Nmax):
            print("Numero de iteraciones excedido")
        break
else:
    print("Intervalo inadecuado")

print("Cero de F(x)  = %f , F(pi)= %.5f"%(pi, func(pi)))




