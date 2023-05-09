import numpy as np
import matplotlib.pyplot as plt
        
x = np.linspace(-10, 10, 2000)
y1 = x**2
y2 = (x-1)**2
        
plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.fill_between(x, y1, y2, where=y1<y2, color='red')
plt.grid()
plt.legend()
plt.show()  

#show intersection points and their values
print('Intersection points:')
for i in range(len(x)):
    if y1[i] == y2[i]:
        print('x =', x[i], 'y =', y1[i])