# Программа, которая позволит с использованием меню обеспечить работу с числовыми массивами:
# 1) Проинициализировать список первыми N элементами заданного в л/р 5 ряда
# 2) Очистить список и ввести его с клавиатуры
# 3) Добавить элемент в произвольное место списка
# 4) Удалить произвольный элемент из списка (по номеру)
# 5) Очистить список
# 6) Найти значение K-го экстремума в списке
# 7) Найти наиболее длинную знакочередующуюся последовательность чётных чисел (Вар. 8)
# Степнов Сергей
# Группа ИУ7-16Б

# Основной список
array = []

while True:
    # Вывод меню
    operation = int(input(
        "Выберите действие:\n"
        "1) Инициализировать список первыми N элементами ряда чисел из 52 варианта л/р 5\n"
        "2) Очистить список и ввести его с клавиатуры\n"
        "3) Добавить элемент в произвольное место списка\n"
        "4) Удалить произвольный элемент из списка\n"
        "5) Очистить список\n"
        "6) Найти значение K-го экстремума в списке\n"
        "7) Найти наиболее длинную знакочередующуюся последовательность чётных чисел\n"
        "0) Выйти из программы\n"
        ">>> "
    ))

    # Проверка на дурака
    if not 0 <= operation <= 7:
        print("\nНет такой команды...\n")
        continue

    # Если вызвана '0' команда - завершение программы
    if operation == 0:
        exit()

    # Проверка на существование элементов в списке
    if not array and operation != 1:
        print("\nДля работы команды необходимо проинициализировать список с помощью команды '1'!\n")
    else:
        if operation == 1:
            # 1) Инициализировать список первыми N элементами ряда чисел из 52 варианта л/р 5
            print("\nИнициализация списка\nЧисловой ряд: 1, 3x^2, 5x^4, ..., (−1)^(n − 1) * (2n + 1) * x^(2n)")
            x = float(input("Введите значение аргумента x: "))
            n = int(input("Введите кол-во элементов ряда: "))

            if n < 1:
                print("\nКол-во элементов числового ряда должно быть больше 0!\n")
            else:
                array.append(1)
                for elem_index in range(1, n):
                    array.append((-1) ** elem_index * (2 * elem_index + 1) * x ** (2 * elem_index))

            print(f"\nЗаданный список:\n{array}\n")
        elif operation == 2:
            # 2) Очистить список и ввести его с клавиатуры
            print("\nВвод нового списка с клавиатуры")

            for index in range(len(array)):
                new_elem = float(input(f"Введите новый элемент списка под номером {index + 1}: "))
                array[index] = new_elem

            print(f"\nНовый список:\n{array}\n")
        elif operation == 3:
            # 3) Добавить элемент в произвольное место списка
            print("\nДобавление элемента в произвольное место списка")
            elem = float(input("Введите значение элемента: "))
            index = int(input("Введите номер в списке: "))

            array.insert(index - 1, elem)

            if index - 1 >= len(array):
                print("\nЭлемент вставлен в конец списка", end="")

            print(f"\nНовый список:\n{array}\n")
        elif operation == 4:
            # 4) Удалить произвольный элемент из списка (по номеру)
            print("\nУдаление элемента из произвольного места в списке")
            index = int(input("Введите номер в списке: "))

            if 0 <= index - 1 < len(array):
                del array[index - 1]
                print(f"\nЭлемент удалён из списка\nНовый список:\n{array}\n")
            else:
                print(f"\nЭлемента с таким номером нет! Возможные значения 1 - {len(array)}\n")
        elif operation == 5:
            # 5) Очистить список
            array.clear()
            print("\nСписок очищен\n")
        elif operation == 6:
            # 6) Найти значение K-го экстремума в списке
            print("\nОтображение K-го экстремума в списке")
            k = int(input("Введите номер экстремума: "))

            extremes = []
            for i in range(1, len(array) - 1):
                if array[i - 1] < array[i] and array[i] > array[i + 1]:
                    extremes.append(array[i])
                elif array[i - 1] <= array[i] and array[i] > array[i + 1]:
                    extremes.append(array[i])
                elif array[i - 1] < array[i] and array[i] >= array[i + 1]:
                    extremes.append(array[i])
                elif array[i - 1] > array[i] and array[i] < array[i + 1]:
                    extremes.append(array[i])
                elif array[i - 1] >= array[i] and array[i] < array[i + 1]:
                    extremes.append(array[i])
                elif array[i - 1] > array[i] and array[i] <= array[i + 1]:
                    extremes.append(array[i])

            if extremes:
                if 0 <= k - 1 < len(extremes):
                    print(f"\nЭкстремум: {extremes[k - 1]}\n")
                else:
                    print(f"\nЭкстремума с таким номером нет! Возможные значения 1 - {len(extremes)}\n")
            else:
                print(f"\nЭкстремумов нет!\n")
        else:
            # 7) Найти наиболее длинную знакочередующуюся последовательность чётных чисел (Вар. 8)
            sequence = []
            temp_sequence = []
            for i in range(len(array) - 1):
                if (array[i] <= 0) != (array[i + 1] <= 0) and array[i] % 2 == 0 and array[i + 1] % 2 == 0:
                    if not temp_sequence:
                        temp_sequence.append(array[i])
                    temp_sequence.append(array[i + 1])
                else:
                    if temp_sequence and len(sequence) < len(temp_sequence):
                        sequence = temp_sequence
                        temp_sequence = []

            if temp_sequence and len(sequence) < len(temp_sequence):
                sequence = temp_sequence
                temp_sequence = []

            if sequence:
                print(f"\nИскомая последовательность:\n{sequence}\n")
            else:
                print("\nТакой последовательности нет\n")
