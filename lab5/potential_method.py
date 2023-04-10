from collections import Counter
from copy import deepcopy

import numpy as np


def balace_cond(a, b, c):
    if (diff := sum(a) - sum(b)) > 0:
        b_new = np.append(b,diff)
        a_new = a
        c_new = np.append(c, [[0] * c.shape[0]], axis=1)
    elif diff < 0:
        b_new = b
        a_new = np.append(a,-diff)
        c_new = np.append(c, [[0] * c.shape[1]], axis=0)
    else:
        a_new = a
        b_new = b
        c_new = c
    return a_new, b_new, c_new


def potential_method(a, b, c):
    a, b, c = balace_cond(a, b, c)
    # Шаг 1. Метод северо-западного угла
    # План перевозок и список базисных позиций
    x = np.zeros((len(a), len(b)))
    B = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        minimum = min([a[i], b[j]])
        x[i, j] = minimum
        B.append((i, j))
        a[i] -= minimum
        b[j] -= minimum
        if a[i] == 0 and i < len(a) - 1:
            i += 1
        elif b[j] == 0:
            j += 1

    # Метод потенциалов
    n, m = len(a), len(b)
    while True:
        A = np.zeros((m + n, m + n))
        b = np.zeros(m + n)
        for num, (i, j) in enumerate(B):
            A[num][i] = 1
            A[num][m + j] = 1
            b[num] = c[i][j]
        A[-1][0] = 1

        # Находим u и v
        u_v = np.linalg.solve(A, b)
        u = u_v[:m]
        v = u_v[m:]

        # Проверка условий оптимальности
        optimal, flag = True, True
        for i in range(m):
            if flag:
                for j in range(n):
                    if u[i] + v[j] > c[i][j]:
                        optimal, flag = False, False
                        B.append((i, j))
                        break
        if optimal:
            return x

        # Удаление строк и столбцов, в которых меньше 2 базисных клеток
        B_copy = deepcopy(B)
        while True:
            i_list = [i for (i, j) in B_copy]
            j_list = [j for (i, j) in B_copy]

            i_counter = Counter(i_list)
            j_counter = Counter(j_list)

            i_to_rm = [i for i in i_counter if i_counter[i] == 1]
            j_to_rm = [j for j in j_counter if j_counter[j] == 1]

            if not i_to_rm and not j_to_rm:
                break
            B_copy = [(i, j) for (i, j) in B_copy if i not in i_to_rm
                      and j not in j_to_rm]

        # Распределение клеток по + и -
        plus, minus = [], []
        plus.append(B_copy.pop())

        while B_copy:
            if len(plus) > len(minus):
                for index, (i, j) in enumerate(B_copy):
                    if plus[-1][0] == i or plus[-1][1] == j:
                        minus.append(B_copy.pop(index))
                        break
            else:
                for index, (i, j) in enumerate(B_copy):
                    if minus[-1][0] == i or minus[-1][1] == j:
                        plus.append(B_copy.pop(index))
                        break

        # Обновление клеток с учетом знаков и Θ
        theta = min(x[i][j] for i, j in minus)
        for i, j in plus:
            x[i][j] += theta
        for i, j in minus:
            x[i][j] -= theta

        for i, j in minus:
            if x[i][j] == 0:
                B.remove((i, j))
                break


