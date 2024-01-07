import numpy as np
from recalculation import recalculation


def delta_check(delta: np.matrix):
    for j in range(delta.shape[1]):
        if delta.tolist()[0][j] < 0:
            return j
    return -1


def main_phase(c: np.matrix, a: np.matrix, x: np.matrix, b: np.matrix):
    b = b-1
    Ab = a[:, np.squeeze(b.tolist())]
    inverse_ab = np.matrix(Ab.I)

    cb = np.matrix([float(c[i, 0]) for i in np.squeeze(b.tolist())]).T

    while True:
        u = cb.T * inverse_ab
        delta = u * a - c.T
        j = delta_check(delta)
        if j == -1:
            return x, b

        z = inverse_ab * a[:, j]
        sigma = [x[0, b[i, 0]] / z[i, 0] if z[i, 0] > 0 else float("inf") for i in range(z.shape[0])]
        sigma_min = min(sigma)
        sigma_min_index = sigma.index(sigma_min)
        if sigma_min == float("inf"):
            raise BaseException("the objective functional of the problem is not bounded "
                                "from above on the set of admissible plans")

        j_star = int(b[sigma_min_index, 0])
        b[sigma_min_index] = j
        x[0, j_star] = 0
        x[0, j] = sigma_min
        for i in range(b.shape[0]):
            if b[i, 0] != j:
                x[0, int(b[i, 0])] -= sigma_min * z[i, 0]

        cb = np.matrix([float(c[i, 0]) for i in np.squeeze(b.tolist())]).T
        Ab[:, sigma_min_index] = a[:, j]

        inverse_ab = recalculation(inverse_ab, a[:, j], sigma_min_index + 1)
        if isinstance(inverse_ab, str):
            return x, b + 1
