import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0,5.0)
x2 = np.linspace(0.0,5.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2) 

plt.subplot(2, 1, 1)
plt.plot(x1,y1, 'o-')
plt.title("A talee of 2 subplots")
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2,y2, 'o-')
plt.title("A talee of 2 subplots")
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()

