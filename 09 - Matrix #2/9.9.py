# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й срез по второму индексу.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from defs import check_int, check_row

# Ввод данных
x = check_int(input("Введите размер X трёхмерного массива: "))
y = check_int(input("Введите размер Y трёхмерного массива: "))
z = check_int(input("Введите размер Z трёхмерного массива: "))
n = check_int(input(f"Введите Y индекс среза трёхмерного массива (1-{y}): "))

if n > y:
    print("Среза с таким значением Y нет в трёхмерном массиве")
    exit()

A = []
max_length = 0
max_length_y = 0

for i in range(x):
    print()
    A.append([])
    for j in range(y):
        row = check_row(input(f"Введите {j + 1} строку {i + 1} слоя массива: ").split(), z, str)
        for g in row:
            g_length = len(g)
            if g_length > max_length:
                max_length = g_length
            if g_length > max_length_y and j == n - 1:
                max_length_y = g_length

        A[i].append(row)

# Вывод
slice_output = ""

print(f"\nТрёхмерный массив:")
for layer in A:
    for matrix_row_index in range(y):
        # Массив
        row = " ".join([format(f"'{elem}'", f">{max_length + 4}") for elem in layer[matrix_row_index]])
        print(f"{' ' * 2 * (x - matrix_row_index)}{row}")
        # Срез
        if matrix_row_index == n - 1:
            slice_output += f"{' ' * 2 * (x - matrix_row_index)}{row}\n"
    print()
    slice_output += "\n"

print(f"\nСрез:\n{slice_output}")
