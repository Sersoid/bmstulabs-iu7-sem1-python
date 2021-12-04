# Требуется написать программу, которая позволит с помощью меню выполнить следующие действия:
# 1) Выбрать файл для работы
# 2) Инициализировать базу данных
# 3) Вывести содержимое базы данных
# 4) Добавить запись в базу данных
# 5) Поиск по одному полю
# 6) Поиск по двум полям
# Тематика базы данных - произвольная, выбираемая на усмотрение исполнителя. Записи должны состоять из 3-4 полей
# разных типов (текстовые, числовые). Поля для поиска в пп. 5 и 6 выбираются на усмотрение исполнителя.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
import os
from labutils.checks import is_int, is_float


def parse_types(split_types: list) -> list:
    data_types = []

    for col_type in split_types:
        if col_type not in ("int", "float", "str"):
            return []
        else:
            if col_type == "int":
                data_types.append(int)
            elif col_type == "float":
                data_types.append(float)
            else:
                data_types.append(str)

    return data_types


def parse_line(db_line: str) -> (list, int):
    split_line = []
    element_max_len = 0
    line_len = len(db_line)
    current_element = ""
    counter = 0

    while counter < line_len:
        if db_line[counter] == ";":
            split_line.append(current_element)
            current_element = ""
            counter += 1
        elif db_line[counter] == "\\" and counter != line_len - 1:
            current_element += db_line[counter + 1]
            counter += 2
        else:
            current_element += line[counter]
            counter += 1
        element_max_len = max(element_max_len, len(current_element))

    element_max_len = max(element_max_len, len(current_element))
    split_line.append(current_element)

    return split_line, element_max_len


def create_db(db_file: str) -> None:
    db_headers = input("Введите названия столбцов таблицы через запятую: ").split(",")
    if db_headers == [""]:
        print("У таблицы должен быть хотя бы один столбец\n")
    else:
        var_types = input("Введите типы данных в заданных столбцах через запятую (int, float или str): ").split(",")
        if len(db_headers) > len(var_types) or var_types == [""]:
            print("Необходимо указать тип данных для каждого столбца\n")
        else:
            var_types_check = parse_types(var_types)
            if not var_types_check:
                print("Указан неизвестный тип данных!\n")
            else:
                var_types = var_types[:len(db_headers)]
                with open(db_file, "w") as new_db:
                    new_db.write(f"{';'.join(var_types)}\n{';'.join(db_headers)}")
                print(f"База данных '{db_file}' создана!\n")


def print_line(db_line: list, db_types: list, element_max_len: int, db_table_size: int) -> None:
    for element_index in range(db_table_size):
        db_value = db_line[element_index]
        db_value_type = db_types[element_index]
        print("│ " + format(f"'{db_value}'" if db_value_type == str else db_value_type(float(db_value)),
                            f'>{element_max_len + 2}') + " ", end="")
    print("│")


current_db = None

while True:
    # Вывод меню
    operation = input(
        "Выберите действие:\n"
        "1) Выбрать файл для работы\n"
        "2) Инициализировать базу данных\n"
        "3) Вывести содержимое базы данных\n"
        "4) Добавить запись в базу данных\n"
        "5) Поиск по одному полю\n"
        "6) Поиск по двум полям\n"
        "0) Выйти из программы\n"
        ">>> "
    )

    if operation == "0":
        # 0) Завершение программы
        exit()
    elif operation == "1":
        # 1) Выбрать файл для работы
        try:
            path = input("\nВведите путь до файла: ")
            temp = open(path, "r")
            temp.close()
            current_db = path
            print(f"Выбрана база данных '{current_db}'\n")
        except FileNotFoundError:
            print("Для работы с данной базой её необходимо создать/инициализировать\n")
    elif operation == "2":
        # 2) Инициализировать базу данных
        method = input("\nВыберите способ:"
                       "\n1) Создать новую базу данных"
                       "\n2) Перезаписать существующую базу"
                       "\n>>> ")

        if method == "1":
            raw_input = input("\nВведите путь до файла новой базы данных (Например ./test.txt): ").split("/")
            db_name = raw_input[-1]
            path = "/".join(raw_input[:-1])
            path = "./" if path == "" else path

            if db_name not in [db for db in os.listdir(path)]:
                current_db = db_name
                create_db(current_db)
            else:
                print("База данных с таким именем уже существует!\n")
        elif method == "2":
            path = input("\nВведите путь до файла: ")
            try:
                temp = open(path, "r")
                temp.close()
                current_db = path
                create_db(path)
            except FileNotFoundError:
                print("Такого файла не существует!\n")
        else:
            print("Нет такой команды...\n")
    elif operation == "3":
        # 3) Вывести содержимое базы данных
        if current_db:
            with open(current_db, "r") as db:
                types = []
                headers = []
                total_max_len = 0
                is_error = False

                for line in db:
                    line, max_len = parse_line(line.strip())
                    total_max_len = max(total_max_len, max_len)
                    if not types:
                        if line != [""]:
                            types = parse_types(line)
                            if not types:
                                print("\nВ выбранной базе указан неизвестный тип данных!\n")
                                is_error = True
                                break
                        else:
                            print("\nВыбранная база данных имеет неверный формат!\n")
                            is_error = True
                            break
                    elif not headers:
                        headers = line
                        break

                if is_error:
                    continue

                if types and headers:
                    table_size = len(headers)

                    print("\n┌", end="")
                    for col_index in range(table_size):
                        print(format(headers[col_index], f"─^{total_max_len + 4}") +
                              ("┬" if col_index < table_size - 1 else "┐\n"), end="")

                    for line in db:
                        line, _ = parse_line(line.strip())
                        print_line(line, types, total_max_len, table_size)

                    print("└" + ("─" * (max_len + 4) + "┴") * (table_size - 1) + "─" * (total_max_len + 4) + "┘\n")
                else:
                    print("\nВыбранная база данных имеет неверный формат!\n")
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    elif operation == "4":
        # 4) Добавить запись в базу данных
        if current_db:
            types = []
            headers = []
            is_error = False

            with open(current_db, "r") as db:
                for line in db:
                    line, _ = parse_line(line.strip())
                    if not types:
                        if line != [""]:
                            types = parse_types(line)
                            if not types:
                                print("\nВ выбранной базе указан неизвестный тип данных!\n")
                                is_error = True
                                break
                        else:
                            print("\nВыбранная база данных имеет неверный формат!\n")
                            is_error = True
                            break
                    elif not headers:
                        headers = line
                        break

            if is_error:
                continue

            if types and headers:
                new_record = []
                is_error = False
                print()

                for param in range(len(headers)):
                    record_value = input(f"Введите значение '{headers[param]}' новой записи: ")

                    if (types[param] == int and is_int(record_value)) or \
                            (types[param] == float and is_float(record_value)):
                        new_record.append(record_value)
                    elif types[param] == str:
                        temp_record_value = ""
                        for char in record_value:
                            if char in ("\\", ";"):
                                temp_record_value += "\\" + char
                            else:
                                temp_record_value += char
                        new_record.append(temp_record_value)
                    else:
                        print("\nВводите корректные данные!!!\n")
                        is_crash = True
                        break

                if is_error:
                    continue

                with open(current_db, "a") as db:
                    db.write("\n" + ";".join(new_record))

                print("\nНовая запись помещена в базу.\n")
            else:
                print("\nВыбранная база данных имеет неверный формат!\n")
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    elif operation == "5" or operation == "6":
        # 5) Поиск по одному полю
        # 6) Поиск по двум полям
        if current_db:
            types = []
            headers = []
            total_max_len = 0
            is_error = False

            with open(current_db, "r") as db:
                for line in db:
                    line, max_len = parse_line(line.strip())
                    total_max_len = max(total_max_len, max_len)
                    if not types:
                        if line != [""]:
                            types = parse_types(line)
                            if not types:
                                print("\nВ выбранной базе указан неизвестный тип данных!\n")
                                is_error = True
                                break
                        else:
                            print("\nВыбранная база данных имеет неверный формат!\n")
                            is_error = True
                            break
                    elif not headers:
                        headers = line
                        break

                if is_error:
                    continue

                if types and headers:
                    col1 = input("\nВведите 1 столбец для поиска: ")
                    if col1 not in headers:
                        print("Нет такого столбца!\n")
                        continue
                    col1_index = headers.index(col1)
                    to_find_col1 = input("Введите значение для поиска в 1 столбце: ")

                    if operation == "6":
                        col2 = input("\nВведите 2 столбец для поиска: ")
                        if col2 not in headers:
                            print("Нет такого столбца!\n")
                            continue
                        col2_index = headers.index(col2)
                        to_find_col2 = input("Введите значение для поиска во 2 столбце: ")
                    else:
                        col2 = col1
                        col2_index = col1_index
                        to_find_col2 = to_find_col1

                    table_size = len(headers)

                    print("\n┌", end="")
                    for col_index in range(table_size):
                        print(format(headers[col_index], f"─^{total_max_len + 4}") +
                              ("┬" if col_index < table_size - 1 else "┐\n"), end="")

                    for line in db:
                        line, _ = parse_line(line.strip())
                        if line[col1_index] == to_find_col1 and line[col2_index] == to_find_col2:
                            print_line(line, types, total_max_len, table_size)

                    print("└" + ("─" * (max_len + 4) + "┴") * (table_size - 1) + "─" * (total_max_len + 4) + "┘\n")
                else:
                    print("\nВыбранная база данных имеет неверный формат!\n")
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    else:
        print("\nНет такой команды...\n")
