# Импорт модулей
from math import sin

# Ввод массивов
D = list(map(int, input("D: ").split()))
F = list(map(int, input("F: ").split()))

A = []
AV = []
L = []
max_j = len(D)
max_k = len(F)

# Основной блок программы
for j in range(max_j):
    avg_sum = 0
    avg_divider = 0
    under_avg_count = 0

    for k in range(max_k):
        if len(A) <= j:
            A.append([])

        value = sin(D[j] + F[k])
        if value > 0:
            avg_sum += value
            avg_divider += 1

        A[j].append(value)

    avg_value = avg_sum / avg_divider

    for i in A[j]:
        if i < avg_value:
            under_avg_count += 1

    AV.append(format(avg_value, ".5g"))
    L.append(under_avg_count)

# Вывод
print("\nМатрица:")

for matrix_row in A:
    print(*[format(i, ">9.5g") for i in matrix_row])

print(f"\nAV: {AV}\nL: {L}")
