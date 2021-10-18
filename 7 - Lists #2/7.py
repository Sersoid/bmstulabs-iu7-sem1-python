# Программа, которая позволит с использованием меню обеспечить работу с числовыми массивами:
# 1) Очистить список и ввести его с клавиатуры
# 2) Добавить элемент в произвольное место списка
# 3) Удалить произвольный элемент из списка
# 4) Очистить список
# 5) Поиск элемента с наибольшим числом подряд идущих пробелов (Вар. 4)
# 6) Замена всех заглавных гласных английских букв на строчные (Вар. 4)
# Степнов Сергей
# Группа ИУ7-16Б

# Основной список
array = []

while True:
    # Вывод меню
    operation = int(input(
        "Выберите действие:\n"
        "1) Очистить список и ввести его с клавиатуры\n"
        "2) Добавить элемент в произвольное место списка\n"
        "3) Удалить произвольный элемент из списка\n"
        "4) Очистить список\n"
        "5) Поиск элемента с наибольшим числом подряд идущих пробелов\n"
        "6) Замена всех заглавных гласных английских букв на строчные\n"
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
    if not array and operation != 1 and operation != 2 and operation != 4:
        print("\nДля работы команды список должен быть не пустым!\n")
    else:
        if operation == 1:
            # 1) Очистить список и ввести его с клавиатуры
            print("\nВвод нового списка с клавиатуры")
            n = int(input("Введите длину нового списка: "))

            array.clear()

            for index in range(n):
                new_elem = input(f"Введите элемент списка под номером {index + 1}: ")
                array.append(new_elem)

            print(f"\nНовый список:\n{array}\n")
        elif operation == 2:
            # 2) Добавить элемент в произвольное место списка
            print("\nДобавление элемента в произвольное место списка")
            elem = input("Введите значение элемента: ")
            index = int(input("Введите номер в списке: "))

            if index >= 1:
                array_length = len(array)
                array_last_elem = array[-1]

                if index - 1 >= array_length:
                    array.append(elem)
                    print("\nЭлемент вставлен в конец списка", end="")
                else:
                    prev_elem = None
                    for i in range(array_length):
                        if index - 1 <= i < array_length:
                            if prev_elem is None:
                                prev_elem = array[i]
                                array[i] = elem
                            else:
                                array[i], prev_elem = prev_elem, array[i]

                        if i == array_length - 1:
                            array.append(array_last_elem)

                print(f"\nНовый список:\n{array}\n")
            else:
                print("\nНельзя вставить элемент в это место списка!\n")
        elif operation == 3:
            # 3) Удалить произвольный элемент из списка
            print("\nУдаление элемента из произвольного места в списке")
            index = int(input("Введите номер в списке: "))

            if 0 <= index - 1 < len(array):
                array_length = len(array)
                for i in range(array_length):
                    if index - 1 <= i < array_length - 1:
                        array[i] = array[i + 1]

                    if i == array_length - 1:
                        del array[-1]

                print(f"\nЭлемент удалён из списка\nНовый список:\n{array}\n")
            else:
                print(f"\nЭлемента с таким номером нет! Возможные значения 1 - {len(array)}\n")
        elif operation == 4:
            # 4) Очистить список
            array.clear()
            print("\nСписок очищен\n")
        elif operation == 5:
            # 5) Поиск элемента с наибольшим числом подряд идущих пробелов
            max_spaces_count = 0
            max_spaces_count_elem = None
            temp_max_spaces_count = 0
            for elem in array:
                for char in elem:
                    if char != " " and temp_max_spaces_count and max_spaces_count < temp_max_spaces_count:
                        max_spaces_count_elem = elem
                        max_spaces_count = temp_max_spaces_count
                        temp_max_spaces_count = 0
                    elif char == " ":
                        temp_max_spaces_count += 1

            if max_spaces_count_elem is None:
                print("\nВ списке нет элементов с пробелами\n")
            else:
                print(f"\nЭлемент с наибольшим количеством подряд идущих пробелов: '{max_spaces_count_elem}'\n")
        else:
            # 6) Замена всех заглавных гласных английских букв на строчные
            for i in range(len(array)):
                new_elem = ""
                for j in range(len(array[i])):
                    ascii_num = ord(array[i][j])
                    if 65 <= ascii_num <= 90:
                        new_elem += chr(ascii_num + 32)
                    else:
                        new_elem += array[i][j]
                array[i] = new_elem

            print(f"\nНовый список:\n{array}\n")
