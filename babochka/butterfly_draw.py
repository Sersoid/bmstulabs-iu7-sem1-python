resolution = 9

matrix_size = int(18 * resolution) // 2 * 2
matrix_left = matrix_size // -2
Matrix = []
for i in range(0, matrix_size):
    Matrix.append([False] * matrix_size)

for x in range(matrix_left, -matrix_left + 1):
    if -9 * resolution <= x <= -8 * resolution:
        y = round((7 * (x / resolution + 8) ** 2 + 1) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-1 / 8 * (x / resolution + 9) ** 2 + 8) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True

    elif -8 * resolution <= x <= -2 * resolution:
        y = round((-1 / 8 * (x / resolution + 9) ** 2 + 8) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((1 / 49 * (x / resolution + 1) ** 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-4 / 63 * (x / resolution) ** 2 + 4 / 63) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round(((x / resolution + 5) ** 2 / 3 - 7) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True

    elif -2 * resolution <= x <= -1 * resolution:
        y = round((-1 / 8 * (x / resolution + 9) ** 2 + 8) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((1 / 49 * (x / resolution + 1) ** 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-4 / 63 * (x / resolution) ** 2 + 4 / 63) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-2 * (x / resolution + 1) ** 2 - 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-1.5 * x / resolution + 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True

    elif -1 * resolution <= x <= 0 * resolution:
        y = round((-4 * (x / resolution) ** 2 + 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((4 * (x / resolution) ** 2 - 6) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-1.5 * x / resolution + 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True

    elif 0 * resolution <= x <= 1 * resolution:
        y = round((-4 * (x / resolution) ** 2 + 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((4 * (x / resolution) ** 2 - 6) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((1.5 * x / resolution + 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True

    elif 1 * resolution <= x <= 2 * resolution:
        y = round((-1 / 8 * (x / resolution - 9) ** 2 + 8) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((1 / 49 * (x / resolution - 1) ** 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-4 / 63 * (x / resolution) ** 2 + 4 / 63) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-2 * (x / resolution - 1) ** 2 - 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((1.5 * x / resolution + 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True

    elif 2 * resolution <= x <= 8 * resolution:
        y = round((-1 / 8 * (x / resolution - 9) ** 2 + 8) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((1 / 49 * (x / resolution - 1) ** 2) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-4 / 63 * (x / resolution) ** 2 + 4 / 63) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round(((x / resolution - 5) ** 2 / 3 - 7) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True

    elif 8 * resolution <= x <= 9 * resolution:
        y = round((7 * (x / resolution - 8) ** 2 + 1) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True
        y = round((-1 / 8 * (x / resolution - 9) ** 2 + 8) * resolution)
        Matrix[-matrix_left - y][-matrix_left + x - 1] = True

tmp = ""
for string in Matrix:
    for var in string:
        if var:
            tmp += "*"
        else:
            tmp += " "
    tmp += "\n"

print(tmp)
