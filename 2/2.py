# Программа для нахождения решений квадратного уравнения вида ax^2 + bx + c = 0 по a, b и c
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
from math import sqrt

# Ввод данных
print("ax^2 + bx + c = 0")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

# Основной блок программы
if a == 0:
    if b == 0:
        if c == 0:
            print("x может принимать любое значение")
        else:
            print("Нет таких значений x, при которых уравнение будет решено")
    else:
        if c == 0:
            print("x = 0")
        else:
            print(f"x = {format(-c / b, '.5g')}")
else:
    if b == 0:
        if c == 0:
            print("x = 0")
        else:
            print(f"x = {format(sqrt(-c / a), '.5g')}")
    else:
        if c == 0:
            print("x1 = 0\n"
                  f"x2 = {format(-b / a, '.5g')}")
        else:
            d = b ** 2 - 4 * a * c
            if d < 0:
                print("Нет таких значений x, при которых уравнение будет решено")
            elif d == 0:
                print(f"x = {format(-b / (2 * a), '.5g')}")
            else:
                print(f"x1 = {format((-b + sqrt(d)) / (2 * a), '.5g')}\n"
                      f"x2 = {format((-b - sqrt(d)) / (2 * a), '.5g')}")
