import numpy as np
from find_inv_matrix_sol import find_inverse_matrix


def dual_simplex_method(c, A, b, B):
    m, n = A.shape
    B = [i - 1 for i in B]
    iteration = 0
    while True:
        iteration += 1

        # Шаги 1-2. Находим матрицу, обратную базисной, и вектор базисных компонент
        if iteration == 1:
            A_b = get_basis_matrix(A, B)
            A_b_inv = np.linalg.inv(A_b)
        else:
            A_b_inv = find_inverse_matrix(A_b, A_b_inv, A[:, B[ind]], ind)
            A_b = get_basis_matrix(A, B)
        c_b = get_basis_vector(c, B)

        # Шаг 3. Найдем базисный допустимый план двойственной задачи.
        if iteration == 1:
            y = np.dot(c_b, A_b_inv)
        else:
            y = y + delta_y*sigma[j_0]

        # Шаг 4. Находим псевдоплан, соответствующий текущему базисному допустимому
        k_b = np.dot(A_b_inv, b)
        k = np.array([0 for _ in range(n)], dtype=np.float64)
        i = 0
        for index in B:
            k[index] = k_b[i]
            i += 1

        # Шаг 5. Проверка псевдоплана на оптимальность
        for elem in k:
            if elem < 0:
                break
        else:
            return k, B

        # Шаг 6. Находим отрицательную компоненту псевдоплана
        j_k = np.argmin(k)
        ind = None
        for index, elem in enumerate(B):
            if elem == j_k:
                ind = index
        delta_y = A_b_inv[ind]

        # Шаг 7. Вычисляем μ для каждого небазисного индекса
        mu = {}
        for j in range(n):
            if j not in B:
                mu[j] = np.dot(delta_y, A[:, j])

        # Шаг 8. Проверка совместности прямой задачи
        check = [el >= 0 for el in mu.values()]
        if all(check):
            print('The direct task is not compatible!')
            return None, None

        # Шаг 9. Находим σ для каждого небазисного индекса, для которого μ отрицательно
        sigma = []
        for key in mu:
            if mu[key] < 0:
                tmp = (c[key] - np.dot(A[:, key], y)) / mu[key]
                sigma.append(tmp)
        sigma = np.asarray(sigma)

        # Шаг 10. Находим индекс, на котором достигается минимум в σ
        j_0 = sigma.argmin()

        # Шаг 11. Заменяем k-й базисный индекс на j0 в B
        B[ind] = j_0


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
