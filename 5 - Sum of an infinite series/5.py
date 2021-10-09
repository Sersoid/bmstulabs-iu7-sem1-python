# Программа для вычисления суммы бесконечного ряда с заданной точностью
# Степнов Сергей
# Группа ИУ7-16Б
# ----------------------------------------------------------------------------------------------------------------------
# Вариант 52
# y = 1 − 3x^2 + 5x^4 + ... + (−1)^(n − 1) * (2n + 1) * x^(2n) + ...
# ----------------------------------------------------------------------------------------------------------------------

# Входные данные
x = float(input("Введите значение аргумента x: "))
eps = float(input("Введите точность: "))
max_iterations = int(input("Введите максимальное кол-во итераций: "))
step = int(input("Введите шаг печати: "))

# Таблица
print(
    "\n┌─────────────┬─────────────┬─────────────┐\n"
    "│ № итерации  │      t      │      S      │\n"
    "├─────────────┼─────────────┼─────────────┤\n"
    "│           1 │           1 │           1 │"
)

S = 1
t = 1
n = 1
while abs(t) >= eps and n < max_iterations:
    t = (-1) ** (n - 1) * (2 * n + 1) * x ** (2 * n)
    if abs(t) < eps:
        break
    S += t
    n += 1

    if n % step == 1 or step == 1:
        print(f"│ {'{:>11}'.format(n)} │ {'{:>11.5g}'.format(t)} │ {'{:>11.5g}'.format(S)} │")

print(
    "└─────────────┴─────────────┴─────────────┘\n"
    f"Сумма бесконечного ряда - {S}, вычислена за {n} итераций."
)
