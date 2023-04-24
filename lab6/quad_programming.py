import numpy as np


def get_basis_vector(c, B):
    i = 0
    c_b = [0 for _ in B]
    for index in B:
            c_b[i] = c[index]
            i += 1
    return c_b


def check(delta_x):
    for i in range(len(delta_x)):
        if delta_x[i] < 0:
            return i
    return -1

def quadr_prog(A, c, x, B, Bs, D):
    while True:
        A_b = A[:, B]
        A_b_inv = np.linalg.inv(A_b)

        # Нахождение промежуточных векторов и проверка оптимальности
        c_x = c + np.dot(x, D)
        c_b = get_basis_vector(c_x, B)
        c_b = [i*(-1) for i in c_b]
        u_x = np.dot(c_b, A_b_inv)
        delta_x = np.dot(u_x, A) + c_x

        j0 = check(delta_x)
        if j0 == -1:
            return x

        # Находим  вектор l
        l = np.zeros(len(x))
        l[j0] = 1
        A_b_ext =A[:, Bs]

        H = np.bmat([
            [D[Bs, :][:, Bs], A_b_ext.T],
            [A_b_ext, np.zeros((len(A), len(A)))]
        ])
        H_inv = np.array(np.linalg.inv(H))

        b_starred = np.concatenate((D[Bs, j0], A[:, j0]))
        x_temp = np.dot(-H_inv, b_starred)
        l[:len(Bs)] = x_temp[:len(Bs)]

        # Находим Θ для каждого элемента множества расширенной опоры ограничений
        sigma = np.dot(np.dot(l, D), l)
        theta = {}
        theta[j0] = np.inf if sigma == 0 else np.abs(delta_x[j0]) / sigma

        for j in Bs:
            if l[j] < 0:
                theta[j] = -x[j] / l[j]
            else:
                theta[j] = np.inf

        j_s = min(theta, key=theta.get)
        theta_0 = theta[j_s]

        # Проверка ограниченности целевой функции
        if theta_0 == np.inf:
            print("'The function is not bounded on the set of admissible plans'")
            return None

        # Обновление допустимого плана
        x = x + theta_0 * l
        if j_s == j0:
            Bs = np.append(Bs, j_s)
        elif j_s in Bs and j_s not in B:
            Bs = np.delete(Bs, j_s)
        elif j_s in B:
            third_condition = False
            s = B.index(j_s)

            # Обновляем опоры ограничений
            for j_plus in set(Bs).difference(B):
                if (np.dot(A_b_inv, A[:, j_plus]))[s] != 0:
                    third_condition = True
                    B[s] = j_plus
                    Bs = np.delete(Bs, j_s)

            if not third_condition:
                B[s] = j0
                Bs[Bs.index(j_s)] = j0
