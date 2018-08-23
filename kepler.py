import numpy as np

G = 6.67e-11
Ms = 1.989e30
AU = 146.6e9
a = 17.834*AU
e = 0.96714
year = 86400*365.25
t_init = 0.0
t_end = 75.32*year
time_array = np.linspace(t_init, t_end, 1000)



def f(E,t):
    value = E - e*np.sin(E) - (G*Ms/a**3)**0.5 * t

    return  value

def dfdE(E):
    value = 1-e*np.cos(E)
    return value

phi_array  = []
r_array = []

Tol = 1.0e-6
Nmax = 1000

for i in range(0, len(time_array)):

    error = 1.0
    iteracion = 0
    xpre =  (G*Ms/a**3)**0.5  * time_array[i] #Anomalia media
    xcurt = 0
    while(error > Tol):
        xcurt = xpre - f(xpre,time_array[i])/dfdE(xpre)
        error = abs(xpre - xcurt)
        iteracion += 1
        
        #print("xpre=%f\t xcurt=%f\t f(xcurt)=% f\t error=%f"%(xpre,xcurt,f(xcurt,time_array[i] ),error))
        xpre = xcurt

        if(iteracion > Nmax):
            print("Numero de iteraciones  excedido")
            break

    phi = 2.0*np.arctan((1+e)/(1-e))**0.5 * np.tan(0.5*xcurt)
    r = a*(1-e**2)/(1+e*np.cos(phi))

    phi_array.append(phi)
    r_array.append(r)


for i in range(0, len(phi_array)):
    print("Phi: %f, r: %f"%(phi_array[i],r_array[i]))
