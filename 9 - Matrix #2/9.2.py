# Найти максимальное значение над главной диагональю и минимальное - под побочной диагональю
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from defs import check_int, check_row, print_matrix

# Ввод данных
n = check_int(input("Введите размер квадратной матрицы: "))

# Основной блок программы
A = []
max_value = None
min_value = None

print()
for i in range(n):
    row = check_row(input(f"Введите {i + 1} строку матрицы: ").split(), n, float)

    for j in range(n):
        if i < j:
            if max_value is None or row[j] > max_value:
                max_value = row[j]
        if j > n - i - 1:
            if min_value is None or row[j] < min_value:
                min_value = row[j]

    A.append(row)

# Вывод
print(f"\nМатрица:")
print_matrix(A, float)
print(f"\nМаксимальное значение над главной диагональю: {'-' if max_value is None else format(max_value, '.5g')}"
      f"\nМинимальное значение под побочной диагональю: {'-' if min_value is None else format(min_value, '.5g')}")
