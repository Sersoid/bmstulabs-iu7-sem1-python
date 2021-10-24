# Программа, которая позволит с использованием меню обеспечить работу с целочисленными матрицами:
# 1) Ввести матрицу
# 2) Добавить строку
# 3) Удалить строку
# 4) Добавить столбец
# 5) Удалить столбец
# 6) Найти строку, имеющую наименьшее количество чётных элементов (Вар. 4)
# 7) Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов
# 8) Найти столбец, где разница между модулями суммы отрицательных и положительных элементов минимальна (Вар. 3)
# 9) Переставить местами столбцы с максимальной и минимальной суммой элементов
# 10) Вывести текущую матрицу
# Степнов Сергей
# Группа ИУ7-16Б


def check_input(raw_input):
    if raw_input:
        if "e" in raw_input and "" in raw_input.split("e"):
            return None
        else:
            processed_input = raw_input.replace("+", "", 1).replace("-", "", 1).replace("e", "", 1).replace(".", "", 1)
            if processed_input.isdigit():
                return int((float(raw_input)))
            else:
                return None
    else:
        return None


def check_list(array, limit):
    result_array = []
    array_length = len(array)

    for index in range(limit if limit else len(array)):
        if index < array_length:
            result = check_input(array[index])
            if result is not None:
                result_array.append(result)
            else:
                return None
        else:
            result_array.append(0)

    return result_array


def print_matrix():
    matrix_print = ""
    for matrix_row in matrix:
        matrix_print += " ".join(map(str, matrix_row)) + "\n"
    return matrix_print


settings = {
    "add_row": True,
    "del_row": True,
    "add_col": True,
    "del_col": True,
}

# Основная матрица
matrix = []

while True:
    # Вывод меню
    operation = input(
        "Выберите действие:\n"
        "1) Ввести матрицу\n"
        "2) Добавить строку\n"
        "3) Удалить строку\n"
        "4) Добавить столбец\n"
        "5) Удалить столбец\n"
        "6) Найти строку, имеющую наименьшее количество чётных элементов\n"
        "7) Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов\n"
        "8) Найти столбец, где разница между модулями суммы отрицательных и положительных элементов минимальна\n"
        "9) Переставить местами столбцы с максимальной и минимальной суммой элементов\n"
        "10) Вывести текущую матрицу\n\n"
        "*) Настройки\n"
        "0) Выйти из программы\n"
        ">>> "
    )

    # Проверка на дурака
    if operation != "*" and (not operation.isdigit() or not 0 <= int(operation) <= 10):
        print("\nНет такой команды...\n")
        continue

    # Если вызвана '0' команда - завершение программы
    if operation == "0":
        exit()

    # сли вызвана '*' команда - открыть настройки
    if operation == "*":
        print("\nНастройки:")
        while True:
            operation = input(
                f"1) Добавление строки средствами python: {'✓' if settings['add_row'] else '⨯'}\n"
                f"2) Удаление строки средствами python: {'✓' if settings['del_row'] else '⨯'}\n"
                f"3) Добавление столбца средствами python: {'✓' if settings['add_col'] else '⨯'}\n"
                f"4) Удаление столбца средствами python: {'✓' if settings['del_col'] else '⨯'}\n"
                "0) Выйти из настроек\n"
                "* > "
            )

            # Проверка на дурака
            if not operation.isdigit() or not 0 <= int(operation) <= 4:
                print("\nНет такой команды...\n")
                continue

            print()

            # Если вызвана '0' команда - выход из настроек
            if operation == "0":
                break
            elif operation == "1":
                settings["add_row"] = not settings["add_row"]
            elif operation == "2":
                settings["del_row"] = not settings["del_row"]
            elif operation == "3":
                settings["add_col"] = not settings["add_col"]
            else:
                settings["del_col"] = not settings["del_col"]
        continue

    # Проверка на существование элементов в списке
    if not matrix and operation != "1" and operation != "2" and operation != "4" and operation != "10":
        print("\nДля работы команды матрица должна быть не пустой!\n")
    elif operation:
        if operation == "1":
            # 1) Ввести матрицу
            n = check_input(input("\nВведите количество строк матрицы: "))
            if n is None:
                print("\nВводите корректные данные!\n")
                continue
            m = check_input(input("Введите количество столбцов матрицы: "))
            if m is None:
                print("\nВводите корректные данные!\n")
                continue

            temp_matrix = []
            is_crash = False

            for i in range(n):
                row = check_list(input("Введите строку матрицы: ").split(), m)
                if row:
                    temp_matrix.append(row)
                else:
                    print("\nВводите корректные данные!\n")
                    is_crash = True
                    continue

            if not is_crash:
                matrix = temp_matrix
                print(f"\nНовая матрица:\n{print_matrix()}")
        elif operation == "2":
            # 2) Добавить строку
            n = check_input(input("\nВведите номер строки матрицы: "))
            if n is None:
                print("\nВводите корректные данные!\n")
                continue

            row = check_list(input("Введите строку матрицы: ").split(), len(matrix[0]) if matrix else None)
            if not row:
                print("\nВводите корректные данные!\n")
                continue

            if n >= 1:
                if settings["add_row"]:
                    matrix.insert(n - 1, row)
                    if n - 1 >= len(matrix):
                        print("\nСтрока вставлена в конец матрицы", end="")
                else:
                    matrix_length = len(matrix)
                    matrix_last_elem = matrix[-1] if matrix_length > 0 else None

                    if n - 1 >= matrix_length:
                        matrix.append(row)
                        print("\nСтрока вставлена в конец матрицы", end="")
                    else:
                        prev_elem = None
                        for i in range(matrix_length):
                            if n - 1 <= i < matrix_length:
                                if prev_elem is None:
                                    prev_elem = matrix[i]
                                    matrix[i] = row
                                else:
                                    matrix[i], prev_elem = prev_elem, matrix[i]
                            if i == matrix_length - 1:
                                matrix.append(matrix_last_elem)
                print(f"\nНовая матрица:\n{print_matrix()}")
            else:
                print("\nНельзя вставить строку в это место матрицы!\n")
        elif operation == "3":
            # 3) Удалить строку
            n = check_input(input("\nВведите номер строки матрицы: "))
            if n is None:
                print("\nВводите корректные данные!\n")
                continue

            if 0 <= n - 1 < len(matrix):
                if settings["del_row"]:
                    del matrix[n - 1]
                else:
                    matrix_length = len(matrix)
                    for i in range(matrix_length):
                        if n - 1 <= i < matrix_length - 1:
                            matrix[i] = matrix[i + 1]
                        if i == matrix_length - 1:
                            del matrix[-1]
                if matrix:
                    print(f"\nСтрока удалена\nНовая матрица:\n{print_matrix()}")
                else:
                    print("\nСтрока удалена\n")
            else:
                print(f"\nСтроки с таким номером нет! Возможные значения 1 - {len(matrix)}\n")
        elif operation == "4":
            # 4) Добавить столбец
            m = check_input(input("\nВведите номер столбца матрицы: "))
            if m is None:
                print("\nВводите корректные данные!\n")
                continue

            col = check_list(input("Введите столбец матрицы: ").split(), len(matrix))
            if not col:
                print("\nВводите корректные данные!\n")
                continue

            if m >= 1:
                if settings["add_col"]:
                    if matrix:
                        for i in range(len(matrix)):
                            matrix[i].insert(m - 1, col[i])
                        if m - 1 >= len(matrix):
                            print("\nСтолбец вставлен в конец матрицы", end="")
                    else:
                        for elem in col:
                            matrix.append([elem])
                else:
                    if matrix:
                        row_length = len(matrix[0])
                        matrix_end = False

                        for i in range(len(matrix)):
                            row_last_elem = matrix[i][-1] if row_length > 0 else None

                            if m - 1 >= row_length:
                                matrix[i].append(col[i])
                                matrix_end = True
                            else:
                                prev_elem = None
                                for j in range(row_length):
                                    if m - 1 <= i < row_length:
                                        if prev_elem is None:
                                            prev_elem = matrix[i][j]
                                            matrix[i][j] = col[i]
                                        else:
                                            matrix[i][j], prev_elem = prev_elem, matrix[i][j]

                                    if i == row_length - 1:
                                        matrix[i].append(row_last_elem)
                        if matrix_end:
                            print("\nСтолбец вставлен в конец матрицы", end="")
                    else:
                        for elem in col:
                            matrix.append([elem])
                print(f"\nНовая матрица:\n{print_matrix()}")
            else:
                print("\nНельзя вставить столбец в это место матрицы!\n")
        elif operation == "5":
            # 5) Удалить столбец
            m = check_input(input("\nВведите номер столбца матрицы: "))
            if m is None:
                print("\nВводите корректные данные!\n")
                continue

            if 0 <= m - 1 < len(matrix[0]):
                if settings["del_col"]:
                    for i in range(len(matrix)):
                        if len(matrix[0]) == 1:
                            del matrix[0]
                        else:
                            del matrix[i][m - 1]
                else:
                    row_length = len(matrix[0])
                    for i in range(len(matrix)):
                        for j in range(row_length):
                            if len(matrix[0]) == 1:
                                del matrix[0]
                            else:
                                if m - 1 <= j < row_length - 1:
                                    matrix[i][j] = matrix[i][j + 1]
                                if j == row_length - 1:
                                    del matrix[i][-1]
                if matrix:
                    print(f"\nСтолбец удалён\nНовая матрица:\n{print_matrix()}")
                else:
                    print("\nСтолбец удалён\n")
            else:
                print(f"\nСтолбца с таким номером нет! Возможные значения 1 - {len(matrix[0])}\n")
        elif operation == "6":
            # 6) Найти строку, имеющую наименьшее количество чётных элементов
            result_row = None
            min_elems = 0
            temp_min_elems = 0

            for i in matrix:
                for j in i:
                    if j % 2 == 0:
                        temp_min_elems += 1

                if not result_row:
                    result_row = i
                    min_elems = temp_min_elems
                elif min_elems > temp_min_elems:
                    result_row = i
                    min_elems = temp_min_elems

                temp_max_elems = 0

            print(f"\nСтрока с наименьшим количеством чётных элементов:\n{' '.join(map(str, result_row))}\n")
        elif operation == "7":
            # 7) Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов
            max_minus_row = None
            min_minus_row = None
            max_minus_elems = None
            min_minus_elems = None
            minus_elems = 0

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] < 0:
                        minus_elems += 1

                if max_minus_elems is None or max_minus_elems < minus_elems:
                    max_minus_row = i
                    max_minus_elems = minus_elems
                if min_minus_elems is None or min_minus_elems > minus_elems:
                    min_minus_row = i
                    min_minus_elems = minus_elems

                minus_elems = 0

            if max_minus_row == min_minus_row:
                print("\nПерестановка строк не нужна\n")
            else:
                matrix[max_minus_row], matrix[min_minus_row] = matrix[min_minus_row], matrix[max_minus_row]
                print(f"\nНовая матрица:\n{print_matrix()}")
        elif operation == "8":
            # 8) Найти столбец, где разница между модулями суммы отрицательных и положительных элементов минимальна
            result_col = []
            temp_result_col = []
            min_delta = None
            plus_sum = 0
            minus_sum = 0

            for j in range(len(matrix[0])):
                for i in range(len(matrix)):
                    temp_result_col.append(matrix[i][j])
                    if matrix[i][j] > 0:
                        plus_sum += matrix[i][j]
                    elif matrix[i][j] < 0:
                        minus_sum -= matrix[i][j]

                if min_delta is None or min_delta > abs(plus_sum - minus_sum):
                    min_delta = abs(plus_sum - minus_sum)
                    result_col = temp_result_col.copy()

                temp_result_col = []
                plus_sum = 0
                minus_sum = 0

            output = '\n'.join(map(str, result_col))
            print(f"\nСтолбец, где разница между модулями суммы отрицательных и положительных элементов минимальна:\n"
                  f"{output}\n")
        elif operation == "9":
            # 9) Переставить местами столбцы с максимальной и минимальной суммой элементов
            max_sum_col = None
            min_sum_col = None
            max_sum = None
            min_sum = None
            temp_sum = 0

            for j in range(len(matrix[0])):
                for i in range(len(matrix)):
                    temp_sum += matrix[i][j]

                if max_sum_col is None and min_sum_col is None:
                    max_sum, min_sum = temp_sum, temp_sum
                    max_sum_col, min_sum_col = j, j
                else:
                    if max_sum < temp_sum:
                        max_sum = temp_sum
                        max_sum_col = j
                    if min_sum > temp_sum:
                        min_sum = temp_sum
                        min_sum_col = j

                temp_sum = 0

            if max_sum_col == min_sum_col:
                print("\nПерестановка столбцов не нужна\n")
            else:
                for i in range(len(matrix)):
                    matrix[i][max_sum_col], matrix[i][min_sum_col] = matrix[i][min_sum_col], matrix[i][max_sum_col]
                print(f"\nНовая матрица:\n{print_matrix()}")
        else:
            # 10) Вывести текущую матрицу
            if matrix:
                print(f"\nМатрица:\n{print_matrix()}")
            else:
                print("\nМатрица не задана\n")
