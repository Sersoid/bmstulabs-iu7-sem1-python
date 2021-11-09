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
    # if search(r"^[+-]?\d*\.?\d+([eE][+-]?\d+)?$", num):
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
    row_length = len(array)

    if row_length < length:
        for _ in range(length - row_length):
            array.append("0")
    elif row_length > length:
        array = array[0:length]

    if elem_type != str:
        for i in range(length):
            if elem_type == int:
                array[i] = check_int(array[i])
            elif elem_type == float:
                array[i] = check_float(array[i])

    return array


def print_matrix_floats(matrix: list, elem_type: type = str, multiplier: int = 1) -> None:
    for matrix_row in matrix:
        if elem_type == str:
            max_length = len(max(matrix_row, key=lambda i: len(i)))
            print(*[format(elem, f">{max_length + 1}") for elem in matrix_row])
        else:
            print(*[format(elem * multiplier, ">13.5g") for elem in matrix_row])
