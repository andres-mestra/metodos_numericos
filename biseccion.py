"""
x^3 + 4x^2 - 10 = 0 en [1,2]
"""

###Funciones auxiliares

#funcion a resolver
def  func(x):
  value = x**3 + 4*x**2-10
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
ai = 1.0
bi = 2.0

#Tolerancia
Tol = 1.0e-4

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
     print("Error = %.5e"%(error))
     iteracion = iteracion+1
     
     print("pi=%f\t ai=%f\t f(pi)=% f\t error=%f"%(pi,ai,func(pi),error))

     if(iteracion > Nmax):
       print("Numero de iteraciones excedido")
       break
else:
   print("Intervalo inadecuado")

print("Cero de F(x)  = %f , F(pi)= %.5f"%(pi, func(pi)))
