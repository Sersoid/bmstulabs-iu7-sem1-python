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


def check_row(array: list, length: int) -> list:
    row_length = len(array)

    if row_length < length:
        for _ in range(length - row_length):
            array.append("0")
    elif row_length > length:
        array = array[0:length]

    for i in range(length):
        array[i] = check_float(array[i])

    return array


def print_matrix_floats(matrix: list, multiplier: int = 1) -> None:
    for matrix_row in matrix:
        print(*[format(elem * multiplier, ">13.5g") for elem in matrix_row])
