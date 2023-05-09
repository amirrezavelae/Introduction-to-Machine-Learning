import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 2000)
y1 = x**2
y2 = (x-1)**2/10**6 + 6*np.log(10)

plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.fill_between(x, y1, y2, where=y1<y2, color='red')
plt.grid()
plt.legend()
plt.show()


