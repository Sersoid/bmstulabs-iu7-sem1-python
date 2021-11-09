# Подсчитать в каждой строке матрицы D количество элементов, превышающих суммы элементов соответствующих строк
# матрицы Z. Разместить эти количества в массиве G, умножить матрицу D на максимальный элемент массива G. Напечатать
# матрицу D до и после преобразования, а также массив G.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from defs import check_int, check_row, print_matrix

# Ввод данных
D_n = check_int(input("Введите кол-во строк матрицы D: "))
D_m = check_int(input("Введите кол-во столбцов матрицы D: "))
Z_n = check_int(input("Введите кол-во строк матрицы Z: "))
Z_m = check_int(input("Введите кол-во столбцов матрицы Z: "))

if D_n > Z_n:
    print("\nКол-во строк матрицы Z должно быть больше или равно кол-ву строк матрицы D")
    exit()

D = []
Z = []
G = []

print()
for i in range(D_n):
    row = check_row(input(f"Введите {i + 1} строку матрицы D: ").split(), D_m, float)
    D.append(row)

print()
for i in range(Z_n):
    row = check_row(input(f"Введите {i + 1} строку матрицы Z: ").split(), Z_m, float)
    Z.append(row)

# Основной блок программы
for i in range(D_n):
    Z_n_sum = sum(Z[i])
    D_n_count = 0

    for j in range(D_m):
        if D[i][j] > Z_n_sum:
            D_n_count += 1

    G.append(D_n_count)

max_G = max(G)

# Вывод
print(f"\nМатрица D:")
print_matrix(D, float)
print(f"\nПреобразованная матрица D:")
print_matrix(D, float, max_G)
print(f"\nМассив G: {G}"
      f"\nМаксимальный элемент массива G: {max_G}")
