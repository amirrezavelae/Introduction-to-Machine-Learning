import numpy as np
import matplotlib.pyplot as plt

X = np.array([
    [4, 0],
    [3, 1],
    [2, 0],
    [3, -1],
    [6, 0],
    [3, 3],
    [0, 0],
    [3, -3],
])
Y = np.array([
    1,
    1,
    1,
    1,
    -1,
    -1,
    -1,
    -1,
])

plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.grid()
plt.show()