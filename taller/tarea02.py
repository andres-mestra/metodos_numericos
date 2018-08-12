import numpy as np

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
resolverSist(np.float16(1.130),
             np.float16(6.990),
             np.float16(1.013),
             np.float16(6.099),
             np.float16(14.20),
             np.float16(4.22))
#1.B



