def check_row(array, length):
    row_length = len(array)
    if row_length < length:
        for _ in range(length - row_length):
            array.append(0)
    elif row_length > length:
        array = array[0:length]

    return array


def print_matrix(matrix):
    for matrix_row in matrix:
        print(*[format(elem, ">9.5g") for elem in matrix_row])


# Ввод
n = int(input("Введите кол-во строк матрицы: "))
m = int(input("Введите кол-во столбцов матрицы: "))

A = []
B = []
C = []
V = []

print()
for i in range(n):
    row = check_row(list(map(float, input(f"Введите {i + 1} строку матрицы A: ").split())), m)
    A.append(row)

print()
for i in range(n):
    row = check_row(list(map(float, input(f"Введите {i + 1} строку матрицы B: ").split())), m)
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
print_matrix(A)

print("\nМатрица B:")
print_matrix(B)

print("\nМатрица C:")
print_matrix(C)

print(f"\nV: {V}")
