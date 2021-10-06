# Программа, которая для заданных по варианту функций выведет таблицу значений этих функций на некотором отрезке и
# построит график одной из них
# Степнов Сергей
# Группа ИУ7-16Б
# ----------------------------------------------------------------------------------------------------------------------
# Вариант 42
# Основное задание:
#   Функция: y = b^9 + 34b^8 - 2b^7 + 24b^6 - 76b^5 + 33b^4 - b^3 + 3b^2 + 7b - 33
#   Начальное значение: -0.8
#   Шаг: 0.05
#   Конечное значение: 1.2
# Дополнительное задание:
#   Найти пару (x, y) при которой значение y минимально
# ----------------------------------------------------------------------------------------------------------------------

# Входные данные
start = float(input("Введите начальное значение: "))  # -0.8
finish = float(input("Введите конечное значение: "))  # 1.2
step = float(input("Введите длину шага: "))  # 0.05
serifs_count = int(input("Введите кол-во засечек на оси графика(4-8): "))  # от 4 до 8
if serifs_count > 8 or serifs_count < 4:
    print("Кол-во засечек должно иметь значение от 4 до 8!!!")
    exit()

# Таблица
print(
    "\ny = b^9 + 34b^8 - 2b^7 + 24b^6 - 76b^5 + 33b^4 - b^3 + 3b^2 + 7b - 33\n"
    "┌─────────────┬─────────────┐\n"
    "│      x      │      y      │\n"
    "├─────────────┼─────────────┤"
)

steps_count = int((finish - start) / step)
min_y = None
x_min_y = None
max_y = None

for step_index in range(steps_count + 1):
    x = start + step * step_index
    y = x ** 9 + 34 * x ** 8 - 2 * x ** 7 + 24 * x ** 6 - 76 * x ** 5 + 33 * x ** 4 - x ** 3 + 3 * x ** 2 + 7 * x - 33

    if min_y is None:
        min_y = y
    if max_y is None:
        max_y = y
    if y < min_y:
        min_y = y
        x_min_y = x
    if y > max_y:
        max_y = y

    print(f"│ {'{:>11.5g}'.format(x)} │ {'{:>11.5g}'.format(y)} │")

print("└─────────────┴─────────────┘")

# График
if min_y > 0 or max_y < 0:
    x_axis = None
else:
    x_axis = int(100 * (-min_y) / (max_y - min_y))

serifs = "\n       "
serif_step = 100 // (serifs_count - 1)
value_step = (max_y - min_y) / (serifs_count - 1)
for i in range(serifs_count):
    serifs += ("{:<" + str(serif_step) + ".5g}").format(min_y + i * value_step)

print(
    f"{serifs}\n   x     \\" + "─" * 98 + "/"
)

for step_index in range(steps_count + 1):
    x = start + step * step_index
    y = x ** 9 + 34 * x ** 8 - 2 * x ** 7 + 24 * x ** 6 - 76 * x ** 5 + 33 * x ** 4 - x ** 3 + 3 * x ** 2 + 7 * x - 33

    point = int(100 * (y - min_y) / (max_y - min_y))
    print("{:>6.5g}".format(x), end='    ')
    if x_axis:
        if x_axis > point:
            if point == 0:
                print(f"○{' ' * (x_axis - 2)}│")
            else:
                print(f"{' ' * (point - 1)}○{' ' * (x_axis - point - 1)}│")
        elif x_axis < point:
            print(f"{' ' * (x_axis - 1)}│{' ' * (point - x_axis - 1)}○")
        else:
            print(f"{' ' * (x_axis - 1)}○")
    else:
        print(f"{' ' * (point - 1)}○")

# Ответ на дополнительный вопрос
print(f"\nМинимальное значение y = {format(min_y, '.5g')} достигается при x = {format(x_min_y, '.5g')}")
