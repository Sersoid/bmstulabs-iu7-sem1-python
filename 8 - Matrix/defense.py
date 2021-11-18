n = int(input("Введите кол-во строк матрицы: "))
m = int(input("Введите кол-во столбцов матрицы: "))

matrix = []
result = []

print()
for i in range(n):
    matrix.append(input(f"Введите {i + 1} строку матрицы: ").split())

for j in range(m):
    count = 0

    for i in range(n):
        for char in matrix[i][j]:
            if char in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                count += 1

    if count % 2 == 1:
        result.append(str(j))

print(f"\nИндексы столбцов, содержащих нечётное количество цифр: {', '.join(result) if result else '-'}")
