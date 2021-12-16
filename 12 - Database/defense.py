# Меню 1) Числа в файл 2) Читать и обрат сортировка в другой файл

while True:
    operation = input(
        "Выберите действие:"
        "\n1) Ввести числа в файл defense1"
        "\n2) Отсортировать в обрат. порядке числа из файла defense1 и записать результат в defense2"
        "\n>>> "
    )

    if operation == "1":
        numbers = input("\nВведите числа через пробел: ").split()

        with open("defense1", "w") as defense1:
            defense1.write("\n".join(numbers))

        print("Числа записаны в файл defense1\n")
    elif operation == "2":
        array = []

        with open("defense1", "r") as defense1:
            for line in defense1:
                array.append(int(line.strip()))

        with open("defense2", "w") as defense2:
            defense2.write("\n".join([str(i) for i in sorted(array, reverse=True)]))

        print("\nЧисла отсортированы и помещены в файл defense2\n")
    else:
        print("\nТакой команды нет!\n")
