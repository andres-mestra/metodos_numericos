import matplotlib.pyplot as plt
import numpy as np 

""" a = np.float64(5)
i = np.float64(1)
while True:
   b = np.float64(a + 10**(-i))
   print("b:%.16f, a:%.16f, i:%.0f "%(b,a,i));
   if a == b:
      break  
   i += 1 """
    
"""
funcion  X(t) = 1.7  y dejando el función de w
"""

###Funciones auxiliares

#funcion a resolver
g = 32.17
t = 1
def  func(x):
  value = (3.4/g)*x**2 + 0.5*(np.exp(x*t) - np.exp(-x*t)) - np.sin(x*t)
  return value


def sign(x):
  if x > 0:
    return 1
  elif x < 0:
    return -1
  else: 
    return 0


###Metodo

#longitud intervalo
ai = -1.0
bi = 1.5

#Tolerancia
Tol = 1.0e-5

#Error inicial
error  = 1.0

#Nmax de interaciones
Nmax = 1000
iteracion = 0

#Verificacion del valor medio

if (sign(func(ai))* sign(func(bi))<0):
    while(error > Tol): 
        pi = 0.5*(ai+bi)
        pi_previo = pi

        #redefinimos los limites del intervalo
        #if(abs(func(pi)) < Tol):
          # print("La raiz del polinomio es %.5f"%(pi))
        #else:
        if(sign(func(pi)) == sign(func(ai))):
            ai = pi
            bi = bi
        elif(sign(func(pi)) == sign(func(bi))):
            ai = ai
            bi = pi

        pi = 0.5*(ai+bi)
        error = abs(pi - pi_previo)
        iteracion = iteracion+1
        
        print("pi=%f\t ai=%f\t f(pi)=% f\t error=%f"%(pi,ai,func(pi),error))

        if(iteracion > Nmax):
            print("Numero de iteraciones excedido")
            break
else:
    print("Intervalo inadecuado")

print("Cero de F(x)  = %f , F(pi)= %.5f"%(pi, func(pi)))

""" 
x1 = np.linspace(-1.5,1.5)
y1  = []


for i in range(0,len(x1)):
  y1.append(func(x1[i]))

fig = plt.figure()
ax = plt.axes()
ax.plot(x1, y1, label='Datos Discretos')
#ax.plot(x_interpol, y_interpol,'.', label='Puntos interpolados')
#ax.plot(x_interpol, np.sin(x_interpol), label='sin(x)')
ax.legend()
plt.show()
"""