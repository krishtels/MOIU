import numpy as np
from first_phase import first_phase

c = np.array([1, 0, 0])
A = np.array([[1, 1, 1],
              [2,2,2]])

b = np.array([-1
                 ,0])

x, B, A, b = first_phase(c, A, b)
print(x)
print(B)
print(A)
print(b)