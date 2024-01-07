import numpy as np


def partial_mul(q: np.matrix, a: np.matrix, k: int) -> np.matrix:
    """ans = []
    for i in range(q.shape[0]):
        ans.append([])
        for j in range(q.shape[1]):
            if i != k:
                ans[i].append(q[i, i] * a[i, j] + q[i, k] * a[k, j])
            else:
                ans[i].append(q[i, i] * a[i,j])"""
    return np.matrix([[q[i, i] * a[i, j] + q[i, k] * a[k, j] if i != k
                       else q[i, i] * a[i, j]
                       for j in range(q.shape[1])] for i in range(q.shape[0])])


def recalculation(matrix: np.matrix, x: np.matrix, i: int):
    i -= 1
    rows, columns = matrix.shape

    if columns != rows or len(matrix.shape) != 2:
        raise ArithmeticError("Matrix isn't square")

    if rows <= i:
        raise AttributeError(f"Matrix doesn't have row with index {i}")
    l = matrix * x
    li = float(l[i])
    if abs(li) < 1e-10:
        raise BaseException("the matrix isn't invertible")
    l[i] = -1
    l *= -1 / li
    e = np.matrix(np.eye(rows))
    e[:, i] = l[:, 0]
    return partial_mul(e, matrix, i)