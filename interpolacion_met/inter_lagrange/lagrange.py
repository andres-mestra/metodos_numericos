import numpy  as np
import matplotlib.pyplot as plt 

"""
x_list = [1,3,5,7,8]
y_list = [5,2,4,1,2]
"""
x_list = [0.0,0.6,0.9]
y_list = [np.log(1+0.0),np.log(1+0.6),np.log(1+0.9)]




def PolyLagrange(x_list,y_list,x):
    sum = 0

    for i in  range(0, len(x_list)):
        prod = 1
        for j in range(0,len(x_list)):
            if(j != i):
                prod = prod*(x - x_list[j])/(x_list[i] - x_list[j])
        sum += y_list[i]*prod

    return sum

print(PolyLagrange(x_list,y_list,0.45))
print(np.log(1+0.45))


"""
x_array = np.linspace(min(x_list), max(x_list),100)
y_array = []



for i in range(0,len(x_array)):
    y_array.append(PolyLagrange(x_list,y_list,x_array[i]))

fig = plt.figure()
ax = plt.axes()
ax.plot(x_list,y_list,'*')
ax.plot(x_array, y_array)
plt.show()
"""