# Ввод
n = int(input("Введите кол-во строк матрицы: "))
m = int(input("Введите кол-во столбцов матрицы: "))

A = []

# Основной блок программы
print()
for i in range(n):
    row = input(f"Введите {i + 1} строку матрицы: ").split()

    row_length = len(row)

    if row_length < n:
        for _ in range(n - row_length):
            row.append(" ")
    elif row_length > n:
        row = row[0:n]

    for j in range(m):
        row[j] = row[j][0]
        if row[j] in ("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"):
            row[j] = "."

    A.append(row)

# Вывод
print("\nМатрица D:")
for matrix_row in A:
    print(*[f"'{i}'" for i in matrix_row])
