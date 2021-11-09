# Поворот квадратной матрицы на 90 градусов по часовой стрелке, затем на 90 градусов против часовой стрелки. Вывести
# промежуточную и итоговую матрицу
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from defs import check_int, check_row, print_matrix

# Ввод данных
n = check_int(input("Введите размер квадратной матрицы: "))

# Основной блок программы
A = []

print()
for i in range(n):
    row = check_row(input(f"Введите {i + 1} строку матрицы: ").split(), n)

    row_length = len(row)
    if row_length < n:
        for _ in range(n - row_length):
            row.append(0)
    elif row_length > n:
        row = row[0:n]

    A.append(row)

# Повороты матрицы
# B - поворот по часовой стрелке
# C - поворот против часовой стрелки
B = []
C = []

for i in range(n):
    B.append([None] * n)
    C.append([None] * n)
    for j in range(n):
        B[i][j] = A[-j - 1][i]
        C[i][j] = A[j][-i - 1]

# Вывод
print("\nИсходная матрица:")
print_matrix(A)
print("\nМатрица, повёрнутая на 90 градусов по часовой стрелке:")
print_matrix(B)
print("\nМатрица, повёрнутая на 90 градусов против часовой стрелки:")
print_matrix(C)
