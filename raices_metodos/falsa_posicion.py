import numpy as np
#Metodo de la falsa posición 

#Resolver: 2 - x + 3*sin(x)
def f(x):
    value = 2 - x + 3*np.sin(x)
    return value

#inputs
p_prev_2 = 0.0 
p_prev_1 = 5.0
Tol = 1.0e-4
error = 1.0
Nmax = 1000
iteraciones  = 0

#Implementación del algorítmo

while(error > Tol):
    p = p_prev_1 - ((p_prev_1 - p_prev_2)*f(p_prev_1)) / (f(p_prev_1) - f(p_prev_2))

    error = abs(p_prev_1 - p)
    print("pn_2 = %f\t  pn_1 = %f\t  p = %f\t f(p) = %f\t error = %f\n"%(p_prev_2 ,p_prev_1 ,p ,abs(f(p)),error));

    if( f(p)*f(p_prev_1) < 0 ):
        p_prev_2 = p_prev_1
        p_prev_1 = p
    elif ( f(p)*f(p-p_prev_1) > 0 ):
        p_prev_1 = p_prev_2
        p_prev_2 = p
    
     
    iteraciones += 1
    if(iteraciones >= Nmax):
        print("El metodo no converge  despues de  %d iteraciones \n"%(Nmax));
        break