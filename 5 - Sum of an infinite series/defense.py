eps = float(input("Введите точность: "))
max_iterations = int(input("Введите максимальное кол-во итераций: "))

S = 1
t = 1
n = 1
while t > eps and n < max_iterations:
    t = 1 / (2 * n)
    if t < eps:
        break
    S += t
    n += 1

if n == max_iterations and abs(t) > eps:
    print("\nЗа указанное число итераций необходимой точности достичь не удалось")
else:
    print(f"\nСумма бесконечного ряда - {S}, вычислена за {n} итераций.")

