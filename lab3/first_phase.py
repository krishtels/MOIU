import numpy as np
from simplex_main_phase import main_phase, get_basis_matrix


def first_phase(c, A, b):
    # Шаг 1. Проверка неотрицательности b
    for index, elem in enumerate(b):
        if elem < 0:
            elem *= -1
            A[index] *= - 1

    m = A.shape[0]
    n = A.shape[1]

    # Шаг 2. Составим вспомогательную задачу линейного программирования
    c_dashed = np.array([0 if i < n else -1 for i in range(n + m)])
    a_dashed = np.append(A, np.eye(m), axis=1)

    # Шаг 3. Построим начальный базисный допустимый план
    x_dashed = np.append(np.array([0 for _ in range(n)]), b)
    B = np.array([n + i + 1 for i in range(m)])

    # Шаг 4. Решим вспомогательную задачу основной фазой симплекс-метода
    x, B = main_phase(c_dashed, a_dashed, x_dashed, B)

    # Шаг 5. Проверка условия совместности
    for i in range(m):
        if x[n + i] != 0:
            print("The problem is not joint!")
            return None, None, None, None

    # Шаг 6. Формируем допустимый план задачи
    x = x[:n]
    while True:
        # Шаг 7. Проверка допустимости текущего базисного плана
        basis = [j <= n for j in B]
        if all(basis):
            return x, B, A, b

        # Шаг 8. Находим максимальный индекс искусственной переменной
        k = np.argmax(B)
        i = B[k] - n

        # Шаг 9. Находим векторы l для каждого индекса от 1 до n, которого нет в В
        A_b = get_basis_matrix(a_dashed, B)
        A_b_inv = np.linalg.inv(A_b)

        l = {}
        for j in range(n):
            if j not in B:
                l[j] = np.dot(A_b_inv, A[:, j])

        # Шаг 10. Преобразование множества базисных индексов
        dependent_row = True
        for j in l:
            if l[j][k] != 0:
                B[k] = j
                dependent_row = False
                break

        # Шаг 11. Удаление линейно зависимых ограничений
        if dependent_row:
            A = np.delete(A, i, 0)
            a_dashed = np.delete(a_dashed, i, 0)
            b = np.delete(b, i)
            B = np.delete(B, k)
