# Написать программу для демонстрации работы метода сортировки (по варианту) на примере массива целых чисел. Программа
# должна состоять из двух частей и выполнять два действия последовательно: сначала отсортировать заданный пользователем
# массив, затем составить таблицу замеров времени сортировки списков трёх различных (заданных пользователем)
# размерностей. Для каждой размерности списка необходимо исследовать:
# 1) случайный список
# 2) отсортированный список
# 3) список, отсортированный в обратном порядке
# Степнов Сергей
# Группа ИУ7-16Б
# Вариант 18: сортировка методом "расчёски"

# Импорт модулей
import random
import time
from labutils.checks import is_int


# Сортировка методом "расчёски"
def hairbrush_sort(array: list, is_reverse: bool = False) -> list:
    step = len(array) - 1
    while step != 0:
        for i in range(0, len(array) - step):
            if array[i] > array[i + step] and not is_reverse or array[i] < array[i + step] and is_reverse:
                array[i], array[i + step] = array[i + step], array[i]
        step = int(step / 1.2473309)
    return array


# Замер времени сортировки переданного массива
def benchmark(array: list, test_num: int) -> float:
    start = time.time_ns()
    hairbrush_sort(array)
    finish = time.time_ns()
    print(f"\r| {'*' * test_num}{'_' * (9 - test_num)} |", end="")
    return (finish - start) / 1e9


# Форматирование вывода ответа в таблице
def value_format(value: float) -> str:
    return format(value, '^11.5g')


# Генерация массива случайных целых чисел
def gen_rand_array(count) -> list:
    border = 10 ** 30
    return [random.randint(-border, border) for _ in range(count)]


# Проверка вводимых данных на int
def int_check(raw_input: str) -> int:
    if is_int(raw_input):
        return int(raw_input)
    else:
        print("Вводите корректные данные!")
        exit()


# Ввод
n1 = int_check(input("Введите размер массива n1: "))
n2 = int_check(input("Введите размер массива n2: "))
n3 = int_check(input("Введите размер массива n3: "))

# Прогресс работы программы
print("\nПрогресс:"
      "\n| _________ |", end="")

# Вывод таблицы
print(
    "\n\n┌───────────────────────┬─────────────┬─────────────┬─────────────┐"
    "\n│                       │      N1     │      N2     │      N3     │"
    "\n├───────────────────────┼─────────────┼─────────────┤─────────────┤"
    "\n│     Упоряд. список    │ "
    f"{value_format(benchmark(list(range(n1)), 1))} │ "
    f"{value_format(benchmark(list(range(n2)), 2))} │ "
    f"{value_format(benchmark(list(range(n3)), 3))} │"
    "\n├───────────────────────┼─────────────┼─────────────┤─────────────┤"
    "\n│      Случ. список     │ "
    f"{value_format(benchmark(gen_rand_array(n1), 4))} │ "
    f"{value_format(benchmark(gen_rand_array(n2), 5))} │ "
    f"{value_format(benchmark(gen_rand_array(n3), 6))} │"
    "\n├───────────────────────┼─────────────┼─────────────┤─────────────┤"
    "\n│ Обрат. упоряд. список │ "
    f"{value_format(benchmark(list(range(n1 - 1, -1, -1)), 7))} │ "
    f"{value_format(benchmark(list(range(n2 - 1, -1, -1)), 8))} │ "
    f"{value_format(benchmark(list(range(n3 - 1, -1, -1)), 9))} │"
    "\n└───────────────────────┴─────────────┴─────────────┴─────────────┘"
)
