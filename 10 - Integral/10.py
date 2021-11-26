# Требуется написать программу для вычисления приближённого значения интеграла двумя разными методами (по варианту).
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
import re


# Проверки на дурака
def check_int(num: str) -> int:
    if num.isdigit():
        return int(num)
    else:
        print(f"\nВводите корректные данные")
        exit()


def check_float(num: str) -> float:
    if re.search(r"[+-]?\d*\.?\d+([eE][+-]?\d+)?", num):
        return float(num)
    else:
        print(f"\nВводите корректные данные")
        exit()


# Функция
def f(x: float) -> float:
    return float(x ** 2)


# Первообразная функции
def f_1(x: float) -> float:
    return 1 / 3 * x ** 3


# Функция вычисления методом 'левых прямоугольников'
def integral_value_triangles(a: float, b: float, partitions: int) -> float:
    h = (b - a) / partitions
    return h * sum([f((a + (i * h))) for i in range(partitions)])


# Функция вычисления методом '3/8'
def integral_value_3_8(a: float, b: float, partitions: int) -> float:
    if partitions % 3 == 0:
        h = (b - a) / partitions
        partitions_sum = 0
        for i in range(partitions + 1):
            if i == 0 or i == partitions:
                partitions_sum += f((a + i * h))
            elif i % 3 == 0:
                partitions_sum += 2 * f((a + i * h))
            else:
                partitions_sum += 3 * f((a + i * h))
        return 3 / 8 * h * partitions_sum
    else:
        return -1.0


# Ввод
start = check_float(input("Введите начало отрезка: "))
finish = check_float(input("Введите конец отрезка: "))
if start >= finish:
    print("\nЗначение начала отрезка должно быть меньше значения конца!")
    exit()

n1 = check_int(input("Введите кол-во разбиений №1: "))
if n1 < 1:
    print("\nКол-во разбиений должно быть больше 0!")
    exit()

n2 = check_int(input("Введите кол-во разбиений №2: "))
if n2 < 1:
    print("\nКол-во разбиений должно быть больше 0!")
    exit()

n1, n2 = sorted((n1, n2))

eps = check_float(input("Введите точность вычисления: "))

# Основной блок программы
# Метод 'левых прямоугольников'
method1_result_1 = integral_value_triangles(start, finish, n1)
method1_result_2 = integral_value_triangles(start, finish, n2)

# Метод '3/8'
method2_result_1 = integral_value_3_8(start, finish, n1)
method2_result_2 = integral_value_3_8(start, finish, n2)

# Вывод №1
print(f"\nN1 = {n1}"
      f"\nN2 = {n2}"
      "\n┌─────────┬─────────────┬─────────────┐"
      "\n│         │      N1     │      N2     │"
      "\n├─────────┼─────────────┼─────────────┤"
      f"\n│ Метод 1 │ {format(method1_result_1, '^11.5g') if method1_result_1 != -1 else format('-', '^11')} │ "
      f"{format(method1_result_2, '^11.5g') if method1_result_2 != -1 else format('-', '^11')} │"
      "\n├─────────┼─────────────┼─────────────┤"
      f"\n│ Метод 2 │ {format(method2_result_1, '^11.5g') if method2_result_1 != -1 else format('-', '^11')} │ "
      f"{format(method2_result_2, '^11.5g') if method2_result_2 != -1 else format('-', '^11')} │"
      "\n└─────────┴─────────────┴─────────────┘")

# Точное значение интеграла
true_integral_value = f_1(finish) - f_1(start)

if method1_result_2 == method2_result_2:
    print("Оба метода показали одинаковый ответ")
    exit()

# Вычисление n для менее точного метода
print("Менее точным является метод 'левых прямоугольников'")

dot2 = 4
dot1_value = integral_value_triangles(start, finish, 2)
dot2_value = integral_value_triangles(start, finish, 4)

while abs(dot1_value - dot2_value) > eps:
    dot2 *= 2
    dot1_value = dot2_value
    dot2_value = integral_value_triangles(start, finish, dot2)

# Вывод №2
print(f"\nТочное значение интеграла: {format(true_integral_value, '.5g')}"
      f"\nЗначение интеграла с точностью {format(eps, '.5g')}: {format(dot2_value, '.5g')}"
      "\nАбсолютная погрешность измерения метода 'левых прямоугольников': "
      f"{format(abs(true_integral_value - method1_result_2), '.5g')}"
      "\nОтносительная погрешность измерения метода 'левых прямоугольников': "
      f"{format(abs(true_integral_value - method1_result_2) / true_integral_value, '.5g')}"
      "\nАбсолютная погрешность измерения метода '3/8': "
      f"{format(abs(true_integral_value - method2_result_2), '.5g')}"
      "\nОтносительная погрешность измерения метода '3/8': "
      f"{format(abs(true_integral_value - method2_result_2) / true_integral_value, '.5g')}"
      f"\nДля менее точного метода кол-во разбиений составило: {dot2}")
