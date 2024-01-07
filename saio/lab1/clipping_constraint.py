import numpy as np
from main_phase import main_phase
from first_phase import first_phase


def clipping_constraint():
    A = np.matrix([[3.0, 2.0, 1.0, 0.0], [-3.0, 2.0, 0.0, 1.0]])
    b = np.matrix([[6.0],
                  [0.0]])
    c = np.matrix([0.0, 1.0, 0.0, 0.0])

    print("Input values: \nA = {0}\nb = {1}\nc = {2}".format(A, b, c))

    x, B = first_phase(c, A, b)
    x, B = main_phase(c.T, A, x, B)
    x, B = np.squeeze(x.tolist()), np.squeeze(B.tolist())
    B = list(B)
    float_value_index = None
    x_fraction_value = None
    for v, elem in enumerate(x):
        if 1-0.00000001 > elem - int(elem) > 0.00000001:
            x_fraction_value = elem - int(elem)
            float_value_index = v
            break

    if float_value_index is None:
        return 'Optimal plan:', x

    k = B.index(float_value_index)
    N = list(set(range(c.shape[1])) - set(B))
    Ab = A[:, B]
    An = A[:, N]
    l = (Ab.I * An)[k, :]

    res = [0] * c.shape[1]
    ind = 0
    for i in N:
        res[i] = l[0, ind]
        ind += 1
    res.append(-1)
    return res, x_fraction_value


print(clipping_constraint())