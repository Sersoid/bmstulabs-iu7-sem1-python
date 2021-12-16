import random
import time


def select_sort(array: list) -> list:
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

    return array


def benchmark(array: list) -> str:
    start = time.time_ns()
    select_sort(array)
    finish = time.time_ns()
    return format((finish - start) / 1e9, ".5g")


n = int(input("Введите размер сортируемого списка: "))

border = 10 ** 5
print(
    f"\nУпоряд. список: {benchmark(list(range(n)))}"
    f"\nСлуч. список: {benchmark([random.randint(-border, border) for _ in range(n)])}"
    f"\nОбрат. упоряд. список: {benchmark(list(range(n - 1, -1, -1)))}"
)
