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


def parse_type(db_type: str) -> Union[tuple[type, str], None]:
    if db_type == "int" or db_type == "q":
        return int, "q"
    elif db_type == "float" or db_type == "d":
        return float, "d"
    elif db_type == "str" or db_type == "s":
        return str, "s"
    else:
        return None


def parse_types(db_types: list) -> Union[tuple[list, int], None]:
    parsed_db_types = []
    db_byte_len = 0

    for db_type in db_types:
        db_type = parse_type(db_type)
        if db_type is not None:
            parsed_db_types.append(db_type)
            if db_type[0] == int:
                db_byte_len += 8
            elif db_type[0] == float:
                db_byte_len += 8
            else:
                db_byte_len += 64
        else:
            print("\nБаза имеет неизвестный тип данных!\n")
            return None

    return parsed_db_types, db_byte_len + len(db_types)


def parse_line(db_line: bytes, db_types: list) -> (list, int):
    db_line = db_line.strip()
    db_split_line = db_line.split(b";")

    try:
        decoded_db_line_data = []

        for i in range(len(db_split_line)):
            if db_types[i][0] == int:
                db_value_format = "q"
            elif db_types[i][0] == float:
                db_value_format = "d"
            elif db_types[i][0] == str:
                db_value_format = "64s"
            else:
                db_value_format = "?"

            db_value = (struct.unpack(db_value_format, db_split_line[i]))[0]
            if db_types[i][0] == str:
                db_value = db_value.replace(b"\x00", b"").decode()

            decoded_db_line_data.append(db_value)

        element_max_len = 0

        for db_value in decoded_db_line_data:
            value_len = len(str(db_value))
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
        db_types = []

        for db_header in db_headers:
            db_type = input(f"Введите тип '{db_header}' новой записи (int, float или str): ")
            db_type_check = parse_type(db_type)
            if db_type_check is not None:
                db_types.append(db_type_check[1])
            else:
                print("\nВведён неизвестный тип данных!\nНе удалось создать базу\n")
                return

        with open(db_file, "wb") as new_db:
            new_db.write(f"{';'.join(db_types)}\n{';'.join(db_headers)}".encode())

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
        else:
            print("│ " + format(db_value, f'>{element_max_len + 2}') + " ", end="")
    print("│")


def print_footer(db_total_max_len: int, db_border: int, db_table_size: int) -> None:
    print(" " * (db_border + 1) + "└" + ("─" * (db_total_max_len + 4) + "┴") * (db_table_size - 1) +
          "─" * (db_total_max_len + 4) + "┘\n")


def print_table(view_num: bool = False) -> int:
    db_types = None
    db_headers = None
    db_table_size = None
    db_records_count = 0

    with open(current_db, "rb") as db:
        db_total_max_len = 0
        for db_line in db:
            if db_types is None:
                db_types, _ = parse_types(db_line.decode().strip().split(";"))
            else:
                if db_headers is None:
                    db_headers = db_line.strip().decode().split(";")
                    db_max_len = max([len(i) for i in db_headers])
                    db_table_size = len(db_headers)
                else:
                    _, db_max_len = parse_line(db_line, db_types)
                    db_records_count += 1
                db_total_max_len = max(db_total_max_len, db_max_len)

    db_border = len(str(db_records_count)) if view_num else -1

    print_header(db_headers, db_total_max_len, db_border, db_table_size)

    is_db_types = True
    is_db_header = True
    with open(current_db, "rb") as db:
        db_line_index = 0
        for db_line in db:
            if is_db_types:
                is_db_types = False
            elif is_db_header:
                is_db_header = False
            else:
                db_line, _ = parse_line(db_line, db_types)
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
            types = None
            headers = None

            with open(current_db, "rb") as db:
                for line in db:
                    if types is None:
                        types, _ = parse_types(line.strip().decode().split(";"))
                    elif headers is None:
                        headers = line.strip().decode().split(";")

            record_values = []
            is_error = False
            print()

            for param in range(len(headers)):
                record_value = input(f"Введите значение '{headers[param]}' новой записи ({types[param][0].__name__}): ")
                try:
                    record_value = types[param][0](record_value)
                except ValueError:
                    print("Введённое значение не соответствует типу записи!")
                    is_error = True
                    break

                if types[param][0] == int:
                    record_type = "q"
                elif types[param][0] == float:
                    record_type = "d"
                elif types[param][0] == str:
                    record_value = record_value.encode()
                    record_len = len(record_value)
                    if record_len >= 64:
                        record_value = record_value[:64]
                        record_type = "64s"
                    else:
                        record_type = f"{64 - record_len}x{record_len}s"
                else:
                    record_type = "?"

                record_values.append(struct.pack(record_type, record_value))

            with open(current_db, "ab") as db:
                db.write(b"\n" + b";".join(record_values))
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

            with open(current_db, "rb+") as db:
                types = db.readline()
                _, byte_len = parse_types(types.decode().strip().split(";"))
                total = len(types) + len(db.readline())
                if records_count == 1:
                    db.truncate(total - 1)
                else:
                    for _ in range(int(record)):
                        byte_string = db.read(byte_len)
                        db.seek(db.tell() - byte_len)
                        db.write(byte_string)
                    new_end = total + (records_count - 1) * byte_len - 1
                    while db.tell() != new_end:
                        db.seek(db.tell() + byte_len)
                        byte_string = db.read(byte_len)
                        db.seek(db.tell() - 2 * byte_len + 1)
                        db.write(byte_string)
                    db.truncate(new_end)
                print("Запись удалена из базы.\n")
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    elif operation == "6" or operation == "7":
        # 6) Поиск по одному полю
        # 7) Поиск по двум полям
        if current_db:
            types = None
            headers = None
            total_max_len = 0

            with open(current_db, "rb") as db:
                for line in db:
                    if types is None:
                        types, _ = parse_types(line.strip().decode().split(";"))
                    else:
                        if headers is None:
                            headers = line.strip().decode().split(";")
                            max_len = max([len(i) for i in headers])
                            table_size = len(headers)
                        else:
                            _, max_len = parse_line(line, types)
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

            print_header(headers, total_max_len, -1, table_size)

            with open(current_db, "rb") as db:
                db.readline()
                db.readline()
                for line in db:
                    line, _ = parse_line(line.strip(), types)
                    if line[col1_index] == to_find_col1 and line[col2_index] == to_find_col2:
                        print_line(line, total_max_len, table_size, -1, -1)

            print_footer(total_max_len, -1, table_size)
        else:
            print("\nПеред использованием данной команды необходимо открыть/инициализировать базу данных\n")
    else:
        print("\nНет такой команды...\n")
