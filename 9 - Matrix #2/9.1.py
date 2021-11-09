# Даны массивы D и F. Сформировать матрицу A по формуле A[j][k] = sin(D[j] + F[k]). Определить среднее арифметическое
# положительных чисел каждой строки матрицы и количество элементов, меньших среднего арифметического. Результаты
# записать соответственно в массивы AV и L. Напечатать матрицу A в виде матрицы и рядом столбцы AV и L.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from math import sin
from defs import check_row, print_matrix_floats

# Ввод данных
D = input("D: ").split()
D = check_row(D, len(D), float)

F = input("F: ").split()
F = check_row(F, len(F), float)

# Основной блок программы
A = []
AV = []
L = []

for j in range(len(D)):
    avg_sum = 0
    avg_divider = 0
    under_avg_count = 0

    for k in range(len(F)):
        if len(A) <= j:
            A.append([])

        value = sin(D[j] + F[k])
        if value > 0:
            avg_sum += value
            avg_divider += 1

        A[j].append(value)

    if avg_divider:
        avg_value = avg_sum / avg_divider
    else:
        avg_value = None

    for i in A[j]:
        if avg_value is not None and i < avg_value:
            under_avg_count += 1

    AV.append("-" if avg_value is None else format(avg_value, ".5g"))
    L.append(str(under_avg_count))

# Вывод
print(f"\nМатрица:")
print_matrix_floats(A, float)
print(f"\nAV: {', '.join(AV)}"
      f"\nL: {', '.join(L)}")
