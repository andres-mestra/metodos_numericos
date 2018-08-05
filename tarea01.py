import matplotlib.pyplot as plt 
import numpy as np 


xT = []
vT = []
aT = []
t = []
eP = []
eK = []

def energiaP(x,k):
    e = 0.5*k*x**2
    return e

def energiaK(v,m):
    e = 0.5*m*v**2
    return  e

def harmonic(A,w):

    for i in range(0,100):  
        x = A*np.cos(w*i)
        v = -A*w*np.sin(w*i)
        a = -A*(w**2)*np.cos(w*i)
        e_p = energiaP(x,2)
        e_k = energiaK(v,3)

        t.append(i)
        xT.append(x)
        vT.append(v) 
        aT.append(a)
        eP.append(e_p)
        eK.append(e_k)



def graficar(x,y,rows,colum,index,color,title,tx,ty):
    plt.subplot(rows,colum,index)
    plt.plot(x, y, '-',c=color)
    plt.title(title)
    plt.xlabel(tx,fontsize=10)
    #plt.axes().set_xscale('log')
    plt.ylabel(ty,fontsize=10)




harmonic(1,2)

plt.figure(figsize=(5,5))
graficar(t,xT,3,1,1,"green","Posición",'t(s)','X(t)')
graficar(t,vT,3,1,2,"red","Velocidad",'t(s)','V(t)')
graficar(t,aT,3,1,3,"orange","Aceleración",'t(s)','a(t)')
plt.figure(figsize=(5,5))
graficar(xT,eP,2,1,1,'blue',"Energia potencial",'X','Ep(x)')
graficar(vT,eK,2,1,2,'red',"Energia cinetica",'V','Ek(x)')
plt.show()



