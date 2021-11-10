# Если можно использовать регулярные выражения:
# from re import search


def check_int(num: str) -> int:
    if num.isdigit():
        return int(num)
    else:
        print(f"\nВводите корректные данные")
        exit()


def check_float(num: str) -> float:
    # Если можно использовать регулярные выражения:
    # if search(r"[+-]?\d*\.?\d+([eE][+-]?\d+)?", num):
    #     return float(num)
    # else:
    #     print(f"\nВводите корректные данные")
    #     exit()

    # Если можно использовать try/except:
    try:
        return float(num)
    except ValueError:
        print(f"\nВводите корректные данные")
        exit()


def check_row(array: list, length: int, elem_type: type = str) -> list:
    length = len(array) if length == -1 else length
    row_length = len(array)

    if row_length < length:
        for _ in range(length - row_length):
            array.append("" if elem_type == str else "0")
    elif row_length > length:
        array = array[0:length]

    if elem_type != str:
        for i in range(length):
            if elem_type == int:
                array[i] = check_int(array[i])
            elif elem_type == float:
                array[i] = check_float(array[i])

    return array


def print_matrix(matrix: list, elem_type: type = str, multiplier: int = 1) -> None:
    max_length = 0
    for matrix_row in matrix:
        max_row_length = 0
        for i in matrix_row:
            elem_length = len(i) if elem_type == str else len(format(i, ".5g"))
            if max_row_length < elem_length:
                max_row_length = elem_length

        if max_row_length > max_length:
            max_length = max_row_length
    for matrix_row in matrix:
        if elem_type == str:
            print(*[format(f"'{elem}'", f">{max_length + 2}") for elem in matrix_row])
        else:
            print(*[format(elem * multiplier, f">{max_length}.5g") for elem in matrix_row])
