# Сформировать матрицу C путём построчного перемножения матриц A и B одинаковой размерности (элементы в i-й строке
# матрицы A умножаются на соответствующие элементы в i-й строке матрицы B), потом сложить все элементы в столбцах
# матрицы C и записать их в массив V.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from defs import check_int, check_row, print_matrix

# Ввод
n = check_int(input("Введите кол-во строк матрицы: "))
m = check_int(input("Введите кол-во столбцов матрицы: "))

# Основной блок программы
A = []
B = []
C = []
V = []

print()
for i in range(n):
    A.append(check_row(input(f"Введите {i + 1} строку матрицы A: ").split(), m, float))

print()
for i in range(n):
    row = check_row(input(f"Введите {i + 1} строку матрицы B: ").split(), m, float)
    B.append(row)
    C.append([])
    for j in range(m):
        C[i].append(A[i][j] * row[j])

for j in range(m):
    col_sum = 0
    for i in range(n):
        col_sum += C[i][j]
    V.append(col_sum)

# Вывод
print("\nМатрица A:")
print_matrix(A, float)
print("\nМатрица B:")
print_matrix(B, float)
print("\nМатрица C:")
print_matrix(C, float)
print(f"\nV: {', '.join([format(i, '.5g') for i in V])}")
