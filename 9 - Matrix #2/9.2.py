# Ввод данных
n = int(input("Введите размер квадратной матрицы: "))

A = []
max_value = None
min_value = None

# Основной блок программы
for i in range(n):
    row = list(map(float, input(f"Введите {i + 1} строку матрицы: ").split()))

    row_length = len(row)
    if row_length < n:
        for _ in range(n - row_length):
            row.append(0)
    elif row_length > n:
        row = row[0:n]

    for j in range(n):
        if i < j:
            if max_value is None or row[j] > max_value:
                max_value = row[j]
        elif i > j:
            if min_value is None or row[j] < min_value:
                min_value = row[j]

    A.append(row)

# Вывод
print("\nМатрица:")

for matrix_row in A:
    print(*[format(i, ">9.5g") for i in matrix_row])

print(f"\nМаксимальное значение над главной диагональю: {max_value}\n"
      f"Минимальное значение под главной диагональю: {min_value}")

