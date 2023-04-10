from potential_method import potential_method
import numpy as np


a = np.array([100, 300, 300])
b = np.array([300, 200, 200])
c = np.array([[8, 4, 1],
              [8, 4, 3],
              [9, 7, 5]])

x = potential_method(a, b, c)
print(x)