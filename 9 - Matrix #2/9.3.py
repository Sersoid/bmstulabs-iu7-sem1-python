# Транспонирование квадратной матрицы
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
    A.append(check_row(input(f"Введите {i + 1} строку матрицы: ").split(), n))

for i in range(n):
    for j in range(n):
        if i < j:
            A[i][j], A[j][i] = A[j][i], A[i][j]

# Вывод
print("\nМатрица:")
print_matrix(A, str)
