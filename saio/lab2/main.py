import numpy as np

A = [[0, 1, 2, 3],
     [0, 0, 1, 2],
     [0, 2, 2, 3]]


def find_max_resourses(A):
    P = len(A)
    Q = len(A[0])

    B = np.zeros((P, Q))
    C = np.zeros((P, Q))

    for p in range(P):
        for q in range(Q):
            if p == 0:
                B[p][q] = A[p][q]
                C[p][q] = q
            else:
                for i in range(q + 1):
                    val = A[p][i] + B[p - 1][q - i]
                    if B[p][q] < val:
                        B[p][q] = val
                        C[p][q] = i

    res = [0] * P
    q = Q - 1
    p = P - 1
    while p >= 0:
        res[p] = int(C[p][q])
        q = q - int(C[p][q])
        p = p - 1

    return int(B[P - 1][Q - 1]), res


print(find_max_resourses(A))
