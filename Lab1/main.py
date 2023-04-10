from find_inv_matrix_sol import *

# test 1
A = np.array([[1, -1, 0],
               [0, 1, 0],
               [0, 0, 1]])
A_inv = np.array([[1, 1, 0],
                   [0, 1, 0],
                   [0, 0, 1]])
x = np.array([[1, 0, 1]]).transpose()
i = 3
print(find_inverse_matrix(A, A_inv, x, i-1))


# test 2
A = np.array([[1, 0, 5],
               [2, 1, 6],
               [3, 4, 0]])
A_inv = np.array([[-24, 20, -5],
                   [18, -15, 4],
                   [5, -4, 1]])
x = np.array([[2, 2, 2]]).transpose()
i = 2
print(find_inverse_matrix(A, A_inv, x, i-1))


# test 3
A = np.array([[1, 0, 5],
               [2, 1, 6],
               [3, 4, 0]])
A_inv = np.array([[-24, 20, -5],
                   [18, -15, 4],
                   [5, -4, 1]])
x = np.array([[0, 0, 0]]).transpose()
i = 2
print(find_inverse_matrix(A, A_inv, x, i-1))
