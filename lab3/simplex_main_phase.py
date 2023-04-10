import numpy as np
from find_inv_matrix_sol import find_inverse_matrix


def get_basis_matrix(A, B):
    A_b = np.zeros((len(B), A.shape[0]))
    i = 0
    for k in B:
        for j in range(len(A)):
            A_b[j][i] = A[j][k]
        i += 1
    return A_b


def get_basis_vector(c, B):
    i = 0
    c_b = [0 for _ in B]
    for index in B:
            c_b[i] = c[index]
            i += 1
    return c_b


def main_phase(c, A, x, B):
    count, A_b = 0, None
    B -= 1
    while True:
        if count == 0:
            A_b = get_basis_matrix(A, B)
            A_b_inv = np.linalg.inv(A_b)
        else:
            A_b_inv = find_inverse_matrix(A_b, A_b_inv, A[:, B[k]], k)
        count += 1
        c_b = get_basis_vector(c, B)

        # Построим вектор потенциалов и вектор оценок
        u_t = np.dot(c_b, A_b_inv)
        delta = np.dot(u_t, A) - c

        # Проверим текущий план на оптимальность
        neg_delta, j0 = None, None
        for i in range(len(delta)):
            # Поиск отрицательной компоненты в векторе оценок
            if delta[i] < 0:
                neg_delta = delta[i]
                j0 = i
                break
        # Если все компоненты положительны оптимальный план найден
        if neg_delta is None:
            return x, B

        # Находим векторы z и theta
        z = np.dot(A_b_inv, A[:, j0])

        theta = np.zeros(len(z))
        for index, item in enumerate(z):
            if item <= 0:
                theta[index] = float('inf')
            else:
                theta[index] = x[B[index]] / z[index]

        # Нахождение минимума в theta и проверка ограниченности целевой функции
        theta_0 = min(theta)
        if theta_0 == float('inf'):
            print('Target function is not limited!')
            return None, None

        # Преобразование базисного допустимого плана
        k = np.argmin(theta)
        j_star = B[k]
        B[k] = j0

        x[j0] = theta_0
        for i in range(A.shape[0]):
            if i != k:
                x[B[i]] -= theta_0 * z[i]
        x[j_star] = 0





