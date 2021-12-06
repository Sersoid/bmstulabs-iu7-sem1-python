import typing


def matrix_size(matrix: typing.Union[typing.List[list]]) -> typing.Tuple[int, int]:
    return len(matrix), len(matrix[0])


def sort_matrix(matrix: typing.Union[typing.List[list]], reverse: bool = False) -> typing.List[list]:
    row_count, col_count = matrix_size(matrix)
    matrix_elements = sorted([matrix[i][j] for j in range(col_count) for i in range(row_count)], reverse=reverse)

    for i in range(row_count):
        for j in range(col_count):
            matrix[i][j] = matrix_elements[i * col_count + j]

    return matrix


def matrix_rotation(matrix: typing.Union[typing.List[list]], clockwise: bool = True) -> typing.List[list]:
    row_count, col_count = matrix_size(matrix)
    matrix_copy = matrix.copy()

    for i in range(col_count):
        for j in range(row_count):
            matrix[i][j] = matrix_copy[-j - 1][i] if clockwise else matrix_copy[j][-i - 1]

    return matrix


def matrix_transposition(matrix: typing.Union[typing.List[list]]) -> typing.List[list]:
    row_count, col_count = matrix_size(matrix)
    if row_count != col_count:
        raise Exception("The matrix must be square")

    for i in range(row_count - 1):
        for j in range(i + 1, col_count):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix
