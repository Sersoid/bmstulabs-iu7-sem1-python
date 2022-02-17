# Дана целочисленная матрица размера NxM. Требуется сформировать новую матрицу размера KxL, переписав в неё все элементы
# исходной по порядку. Если в новую матрицу все элементы не поместятся - лишние отбросить, если ячеек в новой матрице
# больше - дополнить нулевыми элементами.
# Степнов Сергей
# Группа ИУ7-16Б

n = int(input("Введите кол-во строк вводимой матрицы: "))
m = int(input("Введите кол-во столбцов вводимой матрицы: "))

k = int(input("Введите кол-во строк новой матрицы: "))
l = int(input("Введите кол-во столбцов новой матрицы: "))

matrix = []
new_matrix = []

print()
for i in range(n):
    matrix.append(list(map(int, input(f"Введите {i + 1} строку матрицы: ").split())))

for i in range(k):
    row = []

    for j in range(l):
        row_index = (i * l + j) // m
        col_index = (i * l + j) % m
        if row_index < n and col_index < m:
            row.append(matrix[row_index][col_index])
        else:
            row.append(0)

    new_matrix.append(row)

print("\nИсходная матрица: ")
for row in matrix:
    print(*row)
print("\nНовая матрица: ")
for row in new_matrix:
    print(*row)
