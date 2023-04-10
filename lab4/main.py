import numpy as np
from dual_simplex_method import dual_simplex_method


c = np.array([-4, -3, -7, 0, 0])
A = np.array([[-2, -1, -4, 1, 0],
              [-2, -2, -2, 0, 1]])

b = np.array([-1, -1.5])
B = np.array([4, 5])

k, B = dual_simplex_method(c, A, b, B)
print(k)
print(B)