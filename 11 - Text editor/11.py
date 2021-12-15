# Написать программу для выполнения некоторых операций с текстом. Вводить текст не требуется, он должен быть задан в
# исходном тексте программы в виде списка строк (при выводе на экран каждый элемент этого списка должен начинаться с
# новой строки).
# Программа должна позволять с помощью меню выполнить следующие действия:
# 1) Выровнять текст по левому краю
# 2) Выровнять текст по правому краю
# 3) Выровнять текст по ширине
# 4) Удаление заданного слова
# 5) Замена одного слова другим во всём тексте
# 6) Вычисление арифметических операции сложения и вычитания (Номер в журнале чётный)
# 7) Найти предложение, в котором количество слов, содержащих каждую букву 2 и более раз, максимально (Вар. 8)
# Степнов Сергей
# Группа ИУ7-16Б

# Импорт модулей
import re


# Выводит текст
def print_text(input_text: list) -> None:
    max_len = max_line_len(input_text)
    print("┌" + "─" * (max_len + 2) + "┐")
    for line in input_text:
        print(f"│ {line} │")
    print("└" + "─" * (max_len + 2) + "┘\n")


# Возвращает список слов в строке
def split_line(line: str) -> list:
    word_list = re.split(r"\s+", line)
    for word in word_list:
        if word == "":
            word_list.remove("")

    return word_list


# Возвращает длину самой длинной строки
def max_line_len(input_text: list) -> int:
    max_len = 0
    for line in input_text:
        line_len = len(" ".join(split_line(line)))
        if line_len > max_len:
            max_len = line_len

    return max_len


# Выравнивание текста по левому краю
def left_align_line(line: str, max_length: int) -> str:
    word_list = split_line(line)
    line = " ".join(word_list)
    return " ".join(word_list) + " " * (max_length - len(line))


def left_align(input_text: list) -> list:
    result_text = []
    max_len = max_line_len(input_text)

    for line in input_text:
        result_text.append(left_align_line(line, max_len))

    return result_text


# Выравнивание текста по правому краю
def right_align_line(line: str, max_length: int) -> str:
    word_list = split_line(line)
    line = " ".join(word_list)
    return " " * (max_length - len(line)) + " ".join(word_list)


def right_align(input_text: list) -> list:
    result_text = []
    max_len = max_line_len(input_text)

    for line in input_text:
        result_text.append(right_align_line(line, max_len))

    return result_text


# Выравнивание текста по ширине
def width_align_line(line: str, max_length: int) -> str:
    result_line = ""
    word_list = split_line(line)
    line = " ".join(word_list)
    space_count = max_length - len(line)
    space_parts = len(word_list) - 1
    if space_parts:
        const_add = space_count // space_parts
        extra_add = space_count - const_add * space_parts

        for word in word_list[:-1]:
            result_line += word + " " * (const_add + 1 + (1 if extra_add > 0 else 0))
            extra_add -= 1
        result_line += word_list[-1]
    else:
        # Если нужно разместить по центру
        const_add = space_count // 2
        extra_add = space_count - const_add * 2
        result_line = " " * (const_add + (1 if extra_add > 0 else 0)) + word_list[0] + " " * const_add
        # Если не нужно изменять расположение
        # result_line = word_list[0] + " " * space_count

    return result_line


def width_align(input_text: list) -> list:
    result_text = []
    max_len = max_line_len(input_text)

    for line in input_text:
        result_text.append(width_align_line(line, max_len))

    return result_text


def get_answer(expression_array: list) -> str:
    flag = False
    answer = 0
    multi = 1

    for i in expression_array:
        if i == "+":
            multi = 1
        elif i == "-":
            multi = -1
        else:
            flag = True
            answer += multi * int(i)

    if flag:
        return f" {answer} "
    else:
        return ""


# Исходный текст
text = left_align([
    "Он благополучно избегнул встречи с своею хозяйкой на лестнице. Каморка его приходилась под самою кровлей высокого",
    "пятиэтажного дома и походила более на шкаф, чем на квартиру. Квартирная же хозяйка его, у которой он нанимал",
    "эту каморку с обедом и прислугой, помещалась одною лестницей ниже, в отдельной квартире, и каждый раз, при выходе",
    "на улицу, 3 - 2 - 1 ему непременно надо было проходить мимо хозяйкиной кухни, почти всегда настежь отворенной на",
    "два слова",
    "лестницу. И каждый раз молодой человек, проходя мимо, чувствовал какое-то болезненное и трусливое ощущение,",
    "которого",
    "стыдился и от которого морщился. Он был 1-2-3 должен кругом хозяйке и боялся с нею встретиться."
])

text_state = left_align
line_state = left_align_line

while True:
    # Вывод меню
    operation = input(
        "Выберите действие:\n"
        "1) Выровнять текст по левому краю\n"
        "2) Выровнять текст по правому краю\n"
        "3) Выровнять текст по ширине\n"
        "4) Удаление заданного слова\n"
        "5) Замена одного слова другим во всём тексте\n"
        "6) Вычисление арифметических операции сложения и вычитания\n"
        "7) Найти предложение, в котором количество слов, содержащих каждую букву 2 и более раз, максимально\n"
        "0) Выйти из программы\n"
        ">>> "
    )

    if operation == "0":
        # Завершение программы
        exit()
    elif operation == "1":
        # 1) Выровнять текст по левому краю
        if text_state != left_align:
            text = left_align(text)
            text_state = left_align
            line_state = left_align_line
        print_text(text)
    elif operation == "2":
        # 2) Выровнять текст по правому краю
        if text_state != right_align:
            text = right_align(text)
            text_state = right_align
            line_state = right_align_line
        print_text(text)
    elif operation == "3":
        # 3) Выровнять текст по ширине
        if text_state != width_align:
            text = width_align(text)
            text_state = width_align
            line_state = width_align_line
        print_text(text)
    elif operation == "4":
        # 4) Удаление заданного слова
        del_word = input("\nВведите слово для удаления: ")

        for line_index in range(len(text)):
            text_word_list = split_line(text[line_index])
            for text_word in text_word_list:
                if del_word == text_word:
                    text_word_list.remove(del_word)
            text[line_index] = " ".join(text_word_list)

        text = text_state(text)
        print_text(text)
    elif operation == "5":
        # 5) Замена одного слова другим во всём тексте
        rep_word = input("\nВведите заменяемое слово: ")
        pla_word = input("Введите новое слово: ")

        for line_index in range(len(text)):
            text_word_list = split_line(text[line_index])
            for word_index in range(len(text_word_list)):
                additional = "" if text_word_list[word_index][-1] != "," else ","
                if rep_word + additional == text_word_list[word_index]:
                    text_word_list[word_index] = pla_word + additional
            text[line_index] = " ".join(text_word_list)

        text = text_state(text)
        print_text(text)
    elif operation == "6":
        # 6) Вычисление арифметических операции сложения и вычитания
        expressions = []

        for text_line_index in range(len(text)):
            expression = []
            expression_text = ""
            new_line = text[text_line_index]

            for char in text[text_line_index]:
                if char in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", " "):
                    expression_text += char
                    if char != " ":
                        expression.append(char)
                else:
                    if expression:
                        answer = get_answer(expression)
                        if answer:
                            new_line = new_line.replace(expression_text, answer)
                            expressions.append(expression)
                        expression = []
                    expression_text = ""

            text[text_line_index] = new_line

        text = text_state(text)

        if expressions:
            print("\nВсе арифметические выражения в тексте были заменены\n")
        else:
            print("\nВ тексте нет арифметических выражений\n")
    elif operation == "7":
        # 7) Найти предложение, в котором количество слов, содержащих каждую букву 2 и более раз, максимально
        text_word_list = []
        for text_line in text:
            for line_word in split_line(text_line):
                text_word_list.append(line_word)

        sentences = re.split(r"[.?!]", " ".join(text_word_list))[:-1]

        result_sentence = None
        word_count = None

        for sentence in sentences:
            if sentence[0] == " ":
                sentence = sentence[1:]

            sentence_word_count = 0
            for sentence_word in sentence:
                char_count = {}
                for word_char in sentence_word:
                    char_count[word_char] = 1 if word_char not in char_count else char_count[word_char] + 1

                if 1 not in char_count.keys():
                    sentence_word_count += 1

            if word_count is None or word_count < sentence_word_count:
                result_sentence = sentence
                word_count = sentence_word_count

        if result_sentence:
            print(f"\nИскомое предложение:\n{result_sentence}\n")
        else:
            print("\nВ тексте нет слов, содержащих каждую букву 2 и более раз\n")
    else:
        print("\nНет такой команды...\n")
