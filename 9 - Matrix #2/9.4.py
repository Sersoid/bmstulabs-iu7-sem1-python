# Поворот квадратной матрицы на 90 градусов по часовой стрелке, затем на 90 градусов против часовой стрелки. Вывести
# промежуточную и итоговую матрицу.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from copy import deepcopy
from defs import check_int, check_row, print_matrix

# Ввод данных
n = check_int(input("Введите размер квадратной матрицы: "))

A = []

print()
for i in range(n):
    A.append(check_row(input(f"Введите {i + 1} строку матрицы: ").split(), n))

# Вывод №1
print("\nИсходная матрица:")
print_matrix(A)

# Поворот по часовой стрелке
A_copy = deepcopy(A)
for i in range(n):
    for j in range(n):
        A[i][j] = A_copy[-j - 1][i]

# Вывод №2
print("\nМатрица, повёрнутая на 90 градусов по часовой стрелке:")
print_matrix(A)

# Поворот против часовой стрелки
A_copy = deepcopy(A)
for i in range(n):
    for j in range(n):
        A[i][j] = A_copy[j][-i - 1]

print("\nМатрица, повёрнутая на 90 градусов против часовой стрелки:")
print_matrix(A)
