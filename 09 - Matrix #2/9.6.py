# Задана матрица D и массив I, содержащий номера строк, для которых необходимо определить максимальный элемент.
# Значения максимальных элементов запомнить в массиве R. Определить среднее арифметическое вычисленных максимальных
# значений. Напечатать матрицу D, массивы I и R, среднее арифметическое значение.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from defs import check_int, check_row, print_matrix

# Ввод
n = check_int(input("Введите кол-во строк матрицы D: "))
m = check_int(input("Введите кол-во столбцов матрицы D: "))
I_array = check_row(input(f"Введите номера строк матрицы: ").split(), -1, int)

D = []
R_array = []

# Основной блок программы
print()
for i in range(n):
    row = check_row(input(f"Введите {i + 1} строку матрицы D: ").split(), m, float)

    if i + 1 in I_array:
        R_array.append(max(row))

    D.append(row)

# Вывод
print("\nМатрица D:")
print_matrix(D, float)
print(f"\nI: {', '.join([str(i) for i in I_array])}"
      f"\nR: {', '.join([format(i, '.5g') for i in R_array])}"
      f"\nСреднее арифметическое: {format(sum(R_array) / len(R_array), '.5g')}")
