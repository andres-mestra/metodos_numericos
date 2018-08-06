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


def function(dx, fileObj):
    xList = []
    fxList = []
    iList = []
    x = 0
    i = 0
    text = ''
    while x <= 10:
        text += "%d  %e  %e \n" %(iList[i], xList[i], fxList[i])
        iList.append(i)
        xList.append(x)
        fx = np.sin(x)*np.log(x + 1)*np.sinh(x)
        fxList.append(fx)
        x += dx
        i += 1
        
    #for i in range(0,len(iList)):
        #text += "%d  %e  %e \n" %(iList[i], xList[i], fxList[i])
    
    fileObj.write(text)
    fileObj.close()


def factorial(n):
    if n == 0:
        return 1
    else:
        fat = 1
        for i in range(1, n+1):
            fat = fat *i
        
        return  fat 


def cos(x,n):
    resul  = 0
    for i in range(0,n+1):
        resul += (-1)**i * x**(2*i)/factorial(2*i)
    return resul

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
#ax.plot(theta,np.cos(theta))
ax.grid()
ax.set_xlabel(r"$\theta$", fontsize=14)
#plt.show()




def graficar(x,y,rows,colum,index,color,title,tx,ty):
    plt.subplot(rows,colum,index)
    plt.plot(x, y, '-',c=color)
    plt.title(title)
    plt.xlabel(tx,fontsize=10)
    #plt.axes().set_xscale('log')
    plt.ylabel(ty,fontsize=10)


"""
file =   open('data.txt', 'w')
function(0.1, file)
"""


"""
harmonic(1,2)

plt.figure(figsize=(5,5))
graficar(t,xT,3,1,1,"green","Posición",'t(s)','X(t)')
graficar(t,vT,3,1,2,"red","Velocidad",'t(s)','V(t)')
graficar(t,aT,3,1,3,"orange","Aceleración",'t(s)','a(t)')
plt.figure(figsize=(5,5))
graficar(xT,eP,2,1,1,'blue',"Energia potencial",'X','Ep(x)')
graficar(vT,eK,2,1,2,'red',"Energia cinetica",'V','Ek(x)')
plt.show()
"""


