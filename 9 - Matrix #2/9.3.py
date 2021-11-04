# Ввод данных
n = int(input("Введите размер квадратной матрицы: "))

A = []

# Основной блок программы
print()
for i in range(n):
    row = list(map(float, input(f"Введите {i + 1} строку матрицы: ").split()))

    row_length = len(row)
    if row_length < n:
        for _ in range(n - row_length):
            row.append(0)
    elif row_length > n:
        row = row[0:n]

    A.append(row)

for i in range(n):
    for j in range(n):
        if i < j:
            A[i][j], A[j][i] = A[j][i], A[i][j]

# Вывод
print("\nМатрица:")

for matrix_row in A:
    print(*[format(i, ">9.5g") for i in matrix_row])
