import numpy as np


def find_inverse_matrix(A, A_inv, x, i):
    rows, columns = A.shape

    if columns != rows or len(A.shape) != 2:
        raise ArithmeticError("Matrix isn't square")

    if columns <= i:
        raise AttributeError(f"Matrix doesn't have column with index {i}")

    # replace col i to x column vector

    for j in range(len(x)):
        A[j][i] = x[j]

    # Spep 1. l = A_inv * x
    l = np.matmul(A_inv, x)
    if l[i] == 0:
        raise Exception(f"Matrix isn't invertible because l[{i}]==0")

    # Step 2. Copy vector l and change l[i] to -1
    l_copy = np.copy(l)
    l_copy[i] = -1

    # Step 3. Create l_dashed
    l_dashed = -(1 / l[i]) * l_copy

    # Step 4. Q matrix: into E matrix replace colimn i to l_dashed
    Q = np.eye(rows)
    for j in range(len(l_dashed)):
        Q[j][i] = l_dashed[j]

    # Step 5. Res inv matrix = Q*A_inv
    res = mul_matrix(Q, A_inv, i)

    return res


def mul_matrix(q, a_inv, i):
    rows, cols = a_inv.shape
    res = np.zeros([rows, cols])
    for j in range(rows):
        for k in range(cols):
            a = q[j][j] * a_inv[j][k]
            b = q[j][i] * a_inv[i][k]
            res[j][k] = a + b if j != i else a
    return res
