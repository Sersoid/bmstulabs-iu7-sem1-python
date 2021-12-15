# Требуется написать программу, которая позволит с помощью меню выполнить следующие действия по обработке базы данных,
# хранящейся в бинарном файле:
# 1) Выбрать файл для работы
# 2) Инициализировать базу данных
# 3) Вывести содержимое базы данных
# 4) Добавить запись в базу данных
# 5) Удалить запись из базы данных (по номеру в файле)
# 6) Поиск по одному полю
# 7) Поиск по двум полям
# Тематика базы данных - произвольная, выбираемая на усмотрение исполнителя. Записи должны состоять из 3-4 полей разных
# типов (текстовые, числовые). Поля для поиска в пп. 5 и 6 выбираются на усмотрение исполнителя.
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
import os
import struct
from typing import Union
from labutils.checks import is_int


def parse_type(db_type: str) -> Union[type, None]:
    if db_type == "int":
        return int
    elif db_type == "float":
        return float
    elif db_type == "str":
        return str
    elif db_type == "bool":
        return bool
    else:
        return None


def parse_line(db_line: bytes) -> (list, int):
    db_line = db_line.strip()
    db_split_line = db_line.split(b";")
    db_types = db_split_line[0]
    db_line_data = b";".join(db_split_line[1:])

    try:
        db_line_data = struct.unpack(db_types, db_line_data)
        decoded_db_line_data = []
        element_max_len = 0

        for db_value in db_line_data:
            decoded_db_line_data.append(db_value if type(db_value) != bytes else db_value.decode())

        for db_value in decoded_db_line_data:
            value_len = len(str(db_value)) if type(db_value) != bool else (4 if db_value else 5)
            if value_len > element_max_len:
                element_max_len = value_len

        return decoded_db_line_data, element_max_len
    except struct.error:
        return None, 0


def create_db(db_file: str) -> None:
    db_headers = input("Введите названия столбцов таблицы через запятую: ").split(",")
    if db_headers == [""]:
        print("У таблицы должен быть хотя бы один столбец\n")
    else:
        db_headers = [db_value.encode() for db_value in db_headers]
        db_headers_types = ""
        for db_value in db_headers:
            db_headers_types += f"{len(db_value)}s"

        with open(db_file, "wb") as new_db:
            new_db.write((db_headers_types + ";").encode() + struct.pack(db_headers_types, *db_headers))

        print(f"База данных '{db_file}' создана!\n")


def print_header(db_headers: list, db_total_max_len: int, db_border: int, db_table_size: int) -> None:
    print("\n" + " " * (db_border + 1) + "┌", end="")
    for db_col_index in range(db_table_size):
        print(format(db_headers[db_col_index], f"─^{db_total_max_len + 4}") +
              ("┬" if db_col_index < db_table_size - 1 else "┐\n"), end="")


def print_line(db_line: list, element_max_len: int, db_table_size: int, db_border: int, db_line_index: int) -> None:
    if db_border != -1:
        print(f"{db_line_index}{' ' * (db_border - len(str(db_line_index)) + 1)}", end="")
    for element_index in range(db_table_size):
        db_value = db_line[element_index]
        if type(db_value) == str:
            print("│ " + format(f"'{db_value}'", f'>{element_max_len + 2}') + " ", end="")
        elif type(db_value) == bool:
            print("│ " + format("True" if db_value else "False", f'>{element_max_len + 2}') + " ", end="")
        else:
            print("│ " + format(db_value, f'>{element_max_len + 2}') + " ", end="")
    print("│")


def print_footer(db_total_max_len: int, db_border: int, db_table_size: int) -> None:
    print(" " * (db_border + 1) + "└" + ("─" * (db_total_max_len + 4) + "┴") * (db_table_size - 1) +
          "─" * (db_total_max_len + 4) + "┘\n")


def print_table(view_num: bool = False) -> int:
    db_headers = None
    db_table_size = None
    db_records_count = 0

    with open(current_db, "rb") as db:
        db_total_max_len = 0
        for db_line in db:
            if db_headers is None:
                db_headers, db_max_len = parse_line(db_line)
                db_table_size = len(db_headers)
            else:
                _, db_max_len = parse_line(db_line)
                db_records_count += 1
            db_total_max_len = max(db_total_max_len, db_max_len)

    db_border = len(str(db_records_count)) if view_num else -1

    print_header(db_headers, db_total_max_len, db_border, db_table_size)

    is_db_header = True
    with open(current_db, "rb") as db:
        db_line_index = 0
        for db_line in db:
            if is_db_header:
                is_db_header = False
                continue
            db_line, _ = parse_line(db_line)
            print_line(db_line, db_total_max_len, db_table_size, db_border, db_line_index)
            db_line_index += 1

    print_footer(db_total_max_len, db_border, db_table_size)

    return db_records_count


current_db = None

while True:
    # Вывод меню
    operation = input(
        "Выберите действие:\n"
        "1) Выбрать файл для работы\n"
        "2) Инициализировать базу данных\n"
        "3) Вывести содержимое базы данных\n"
        "4) Добавить запись в базу данных\n"
        "5) Удалить запись из базы данных\n"
        "6) Поиск по одному полю\n"
        "7) Поиск по двум полям\n"
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
            raw_input = input("\nВведите путь до файла новой базы данных (Например ./students): ").split("/")
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
            print_table()
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    elif operation == "4":
        # 4) Добавить запись в базу данных
        if current_db:
            headers = None

            with open(current_db, "rb") as db:
                if headers is None:
                    headers, _ = parse_line(db.readline())

            new_record_types = ""
            new_record_values = []
            is_error = False
            print()

            for param in range(len(headers)):
                record_type = input(f"Введите тип '{headers[param]}' новой записи (int, float, str или bool): ")
                record_type = parse_type(record_type)
                if record_type is None:
                    print("Введён неизвестный тип данных!\n")
                    is_error = True
                    break

                record_value = input(f"Введите значение '{headers[param]}' новой записи: ")
                try:
                    record_value = record_type(record_value) if record_type != str \
                        else record_type(record_value).encode()
                except ValueError:
                    print("Введённое значение не соответствует типу записи!")
                    is_error = True
                    break

                if record_type == int:
                    new_record_types += "56xq"
                elif record_type == float:
                    new_record_types += "56xd"
                elif record_type == str:
                    record_len = len(record_value)
                    if record_len >= 64:
                        record_value = record_value[:64]
                        new_record_types += "64s"
                    else:
                        new_record_types += f"{64 - record_len}x{record_len}s"
                elif record_type == bool:
                    new_record_types += "63x?"

                new_record_values.append(record_value)

            if is_error:
                print("Не удалось поместить запись в базу\n")
            else:
                with open(current_db, "ab") as db:
                    db.write(f"\n{new_record_types};".encode() + struct.pack(new_record_types, *new_record_values))
                print("Новая запись помещена в базу.\n")
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    elif operation == "5":
        if current_db:
            records_count = print_table(True)
            record = input("Введите номер строки для удаления: ")

            if not is_int(record) or is_int(record) and not 0 <= int(record) < records_count:
                print("В таблице нет строки с таким номером\n")
                continue

            ...
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    elif operation == "6" or operation == "7":
        # 6) Поиск по одному полю
        # 7) Поиск по двум полям
        if current_db:
            headers = None
            total_max_len = 0

            with open(current_db, "rb") as db:
                for line in db:
                    if headers is None:
                        headers, max_len = parse_line(line)
                        table_size = len(headers)
                    else:
                        _, max_len = parse_line(line)
                    total_max_len = max(total_max_len, max_len)

            col1 = input("\nВведите 1 столбец для поиска: ")
            if col1 not in headers:
                print("Нет такого столбца!\n")
                continue
            col1_index = headers.index(col1)
            to_find_col1 = input("Введите значение для поиска в 1 столбце: ")

            if operation == "7":
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
            print_header(headers, total_max_len, -1, table_size)

            with open(current_db, "rb") as db:
                db.readline()
                for line in db:
                    line, _ = parse_line(line.strip())
                    if line[col1_index] == to_find_col1 and line[col2_index] == to_find_col2:
                        print_line(line, total_max_len, table_size, -1, -1)

            print_footer(total_max_len, -1, table_size)
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    else:
        print("\nНет такой команды...\n")
