# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимоопределитьмаксимальныйэлемент.Значениямаксимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленныхмаксимальныхзначений.НапечататьматрицуD,массивыIиR,
# среднее арифметическое значение.

# Ввод
n = int(input("Введите кол-во строк матрицы D: "))
m = int(input("Введите кол-во столбцов матрицы D: "))
I_array = list(map(int, input("Введите номера строк матрицы: ").split()))

D = []
R_array = []

# Основной блок программы
for i in range(n):
    row = list(map(float, input(f"Введите {i + 1} строку матрицы: ").split()))

    row_length = len(row)
    if row_length < n:
        for _ in range(n - row_length):
            row.append(0)
    elif row_length > n:
        row = row[0:n]

    if i + 1 in I_array:
        R_array.append(max(row))

    D.append(row)

# Вывод
print("\nМатрица D:")
for matrix_row in D:
    print(*[format(i, ">9.5g") for i in matrix_row])

print(f"\nI: {I_array}"
      f"\nR: {R_array}"
      f"\nСреднее арифметическое: {sum(R_array) / len(R_array)}")
