import numpy as np
from quad_programming import quadr_prog

c = np.array([-8, -6, -4, -6])
A = np.array([[1, 0, 2, 1],
              [0, 1, -1, 2]])
x = np.array([2, 3, 0, 0])
B = np.array([0, 1])
Bs = np.array([0, 1])
D = np.array([[2, 1, 1, 0],
              [1, 1, 0, 0],
              [1, 0, 1, 0],
              [0, 0, 0, 0]])
x = quadr_prog(A, c, x, B, Bs, D)
print(x)


