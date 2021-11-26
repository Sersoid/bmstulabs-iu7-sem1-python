# Найти значение интеграла функции y = sin(x) методом серединных прямоугольников с заданным числом разбиений
from math import sin


def f(x):
    return sin(x)


a = float(input("Введите начало отрезка: "))
b = float(input("Введите конец отрезка: "))
n = int(input("Введите кол-во разбиений: "))

h = (b - a) / n
print(f"\nЗначение интеграла: "
      f"{format(h * sum([f((2 * a + (i - 1) * h + i * h) / 2) for i in range(1, n + 1)]), '.5g')}")
