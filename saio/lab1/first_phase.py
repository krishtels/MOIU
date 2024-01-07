import numpy as np
from main_phase import main_phase


def first_phase(c: np.matrix, A: np.matrix, b: np.matrix):

    for i in range(len(b)):
        if b[i, 0] < 0:
            A[i, :] *= -1
            b[i, 0] *= -1

    m, n = A.shape
    c_ = np.matrix([0] * n + [-1] * m).T
    AHorz = np.zeros((m, n + m)).astype('float')
    AHorz[0:m, 0:n] = A
    AHorz[0:m, n: n+m] = np.eye(m)
    AHorz = np.matrix(AHorz)

    x = np.matrix([0.0] * n + list(np.squeeze(b.tolist())))
    B = np.matrix([i for i in range(n, n + m)]).T + 1

    x_, B = main_phase(c_, AHorz, x, B)

    if len(np.flatnonzero(x_[:, n:])) != 0:
        raise "task is not feasible"

    x = x_[:, :n]

    while True:
        if max(B) < n:
            return x, B + 1

        k = list(np.squeeze(B.tolist())).index(float(max(B)))
        i = max(B) - n
        l = []
        Ab = AHorz[:, np.squeeze(B.tolist())]
        inverse_ab = Ab.getI()
        for j in set(range(n)) - set(np.squeeze(B.tolist())):
            l.append(inverse_ab * AHorz[:, j])

        ok = True
        for j in l:
            if j[k, 0] != 0:
                ok = False
                B[k] = i
                break
        if ok:
            A = np.matrix(np.delete(A.getA(), i, 0))
            b = np.matrix(np.delete(b.getA(), i, 0))
            B = np.matrix(np.delete(B.getA(), i, 0))
            AHorz = np.matrix(np.delete(AHorz.getA(), i, 0))
