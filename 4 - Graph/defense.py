# Написать программу, которая построит график функции '2sin(3x) / (cos(x)^2 + 1)' в указанном диапазоне с длиной шагом
# Степнов Сергей
# Группа ИУ7-16Б

from math import sin, cos

start = float(input("Введите начальное значение: "))
finish = float(input("Введите конечное значение: "))
if start > finish:
    start, finish = finish, start
step = float(input("Введите длину шага: "))

min_y = None
max_y = None
steps_count = int((finish - start) / step)
coords = []

for step_index in range(steps_count + 1):
    x = start + step * step_index
    y = 2 * sin(3 * x) / (cos(x) ** 2 + 1)

    if min_y is None:
        min_y = y
    if max_y is None:
        max_y = y

    if y < min_y:
        min_y = y
        x_min_y = x
    if y > max_y:
        max_y = y

    coords.append((x, y))

print(
    f"\n             {'{:<53.5g}'.format(min_y)}{'{:>53.5g}'.format(max_y)}\n     b      ┌──\\" + "─" * 98 + "/"
)

if min_y > 0 or max_y < 0:
    x_axis = None
else:
    x_axis = int(100 * (-min_y) / (max_y - min_y))

for xy_pair in coords:
    point = int(100 * (xy_pair[1] - min_y) / (max_y - min_y))
    print("{:>11.5g}".format(xy_pair[0]), end=' │  ')
    if x_axis:
        if x_axis > point:
            if point == 0:
                print(f"*{' ' * (x_axis - 2)}│")
            else:
                print(f"{' ' * (point - 1)}*{' ' * (x_axis - point - 1)}│")
        elif x_axis < point:
            print(f"{' ' * (x_axis - 1)}│{' ' * (point - x_axis - 1)}*")
        else:
            print(f"{' ' * (x_axis - 1)}*")
    else:
        print(f"{' ' * (point - 1)}*")

print("─" * 12 + "┴──/" + "─" * 98 + "\\")
