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

B = []

for i in range(n):
    B.append([None] * n)
    for j in range(n):
        B[i][j] = A[-j - 1][i]

# Вывод
print("\nИсходная матрица:")
for matrix_row in A:
    print(*[format(i, ">9.5g") for i in matrix_row])

print("\nМатрица, повёрнутая на 90 градусов по часовой стрелке:")
for matrix_row in B:
    print(*[format(i, ">9.5g") for i in matrix_row])
