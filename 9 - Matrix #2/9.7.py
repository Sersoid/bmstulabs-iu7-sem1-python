# Дана матрица символов. Заменить в ней все гласные английские буквы на точки.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from defs import check_int, check_row, print_matrix

# Ввод
n = check_int(input("Введите кол-во строк матрицы: "))
m = check_int(input("Введите кол-во столбцов матрицы: "))

A = []

# Основной блок программы
print()
for i in range(n):
    row = check_row(input(f"Введите {i + 1} строку матрицы: ").split(), m, str)

    for j in range(m):
        if row[j][0] in ("a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"):
            row[j] = "."
        else:
            row[j] = row[j][0]

    A.append(row)

# Вывод
print("\nМатрица:")
print_matrix(A)
