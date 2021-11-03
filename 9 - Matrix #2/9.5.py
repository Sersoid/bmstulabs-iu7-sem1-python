def check_row(array, length):
    row_length = len(array)
    if row_length < length:
        for _ in range(length - row_length):
            array.append(0)
    elif row_length > length:
        array = array[0:length]

    return array


D_n = int(input("Введите кол-во строк матрицы D: "))
D_m = int(input("Введите кол-во столбцов матрицы D: "))
Z_n = int(input("Введите кол-во строк матрицы Z: "))
Z_m = int(input("Введите кол-во столбцов матрицы Z: "))

if D_n > Z_n:
    print("\nКол-во строк матрицы Z должно быть больше или равно кол-ву строк матрицы D")
    exit()

D = []
Z = []
G = []

print()
for i in range(D_n):
    row = check_row(list(map(float, input(f"Введите {i + 1} строку матрицы D: ").split())), D_m)
    D.append(row)

print()
for i in range(Z_n):
    row = check_row(list(map(float, input(f"Введите {i + 1} строку матрицы Z: ").split())), Z_m)
    Z.append(row)

for i in range(D_n):
    Z_n_sum = sum(Z[i])
    D_n_count = 0

    for j in range(D_m):
        if D[i][j] > Z_n_sum:
            D_n_count += 1

    G.append(D_n_count)

# Вывод
print("\nМатрица D:")
for matrix_row in D:
    print(*[format(i, ">9.5g") for i in matrix_row])

max_G = max(G)

print("\nМатрица умноженная на максимальный элемент массива G:")
for matrix_row in D:
    print(*[format(i * max_G, ">9.5g") for i in matrix_row])

print(f"\nМассив G: {G}"
      f"\nМаксимальный элемент: {max_G}")
