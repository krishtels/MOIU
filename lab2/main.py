import numpy as np
from simplex_main_phase import main_phase

c = np.array([1, 1, 0, 0, 0])
A = np.array([[-1, 1, 1, 0, 0],
              [1, 0, 0, 1, 0],
              [0, 1, 0, 0, 1]])
x = np.array([0, 0, 1, 3, 2])
b = np.array([1, 3, 2])
B = np.array([3, 4, 5])

x, B = main_phase(c, A, x, B)
print(x)
print(B)



c = np.array([0, 0, 0, -1, -1])
A = np.array([[1, 1, 1, 1, 0],
              [2, 2, 2, 0, 1]])
x = np.array([0, 0, 0, 0, 0])
b = np.array([1, 3, 2])
B = np.array([4, 5])
x, B = main_phase(c, A, x, B)
print(x)
print(B)