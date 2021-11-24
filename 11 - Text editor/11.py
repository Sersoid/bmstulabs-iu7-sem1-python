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


# Проверки на дурака
def check_int(num: str) -> int:
    if num.isdigit():
        return int(num)
    else:
        print(f"\nВводите корректные данные")
        exit()


def check_float(num: str) -> float:
    if re.search(r"[+-]?\d*\.?\d+([eE][+-]?\d+)?", num):
        return float(num)
    else:
        print(f"\nВводите корректные данные")
        exit()


# Выводит текст
def print_text(input_text: str) -> None:
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
def left_align(input_text: list) -> list:
    result_text = []

    for line in input_text:
        word_list = split_line(line)
        line = " ".join(word_list)
        result_text.append(" ".join(word_list) + " " * (max_line_len(input_text) - len(line)))

    return result_text


# Выравнивание текста по правому краю
def right_align(input_text: list) -> list:
    result_text = []

    for line in input_text:
        word_list = split_line(line)
        line = " ".join(word_list)
        result_text.append(" " * (max_line_len(input_text) - len(line)) + " ".join(word_list))

    return result_text


# Выравнивание текста по ширине
def width_align(input_text: list) -> list:
    result_text = []

    max_len = max_line_len(input_text)

    for line in input_text:
        result_line = ""
        word_list = split_line(line)
        line = " ".join(word_list)
        space_count = max_len - len(line)
        space_parts = len(word_list) - 1
        const_add = space_count // space_parts
        extra_add = space_count - const_add * space_parts

        for word in word_list[:-1]:
            result_line += word + " " * (const_add + 1 + (1 if extra_add > 0 else 0))
            extra_add -= 1
        result_line += word_list[-1]

        result_text.append(result_line)

    return result_text

# Исходный текст
text = left_align([
    "Он благополучно избегнул встречи с своею хозяйкой на лестнице. Каморка его приходилась под самою кровлей высокого",
    "пятиэтажного дома и походила более на шкаф, чем на квартиру. Квартирная же хозяйка его, у которой он нанимал",
    "эту каморку с обедом и прислугой, помещалась одною лестницей ниже, в отдельной квартире, и каждый раз, при выходе",
    "1   +    2 + 3",
    "на улицу, ему непременно надо было проходить мимо хозяйкиной кухни, почти всегда настежь отворенной на",
    "лестницу. И каждый раз молодой человек, проходя мимо, чувствовал какое-то болезненное и трусливое ощущение,",
    "которого стыдился и от которого морщился. Он был должен 1e10-2e6+1 кругом хозяйке и боялся с нею встретиться."
])

text_state = left_align

while True:
    # Вывод меню
    operation = check_int(input(
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
    ))

    if operation == 0:
        # Завершение программы
        exit()
    elif operation == 1:
        # 1) Выровнять текст по левому краю
        if text_state != left_align:
            text = left_align(text)
            text_state = left_align
        print_text(text)
    elif operation == 2:
        # 2) Выровнять текст по правому краю
        if text_state != right_align:
            text = right_align(text)
            text_state = right_align
        print_text(text)
    elif operation == 3:
        # 3) Выровнять текст по ширине
        if text_state != width_align:
            text = width_align(text)
            text_state = width_align
        print_text(text)
    elif operation == 4:
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
    elif operation == 5:
        # 5) Замена одного слова другим во всём тексте
        rep_word = input("\nВведите заменяемое слово: ")
        pla_word = input("Введите новое слово: ")

        for line_index in range(len(text)):
            text_word_list = split_line(text[line_index])
            for word_index in range(len(text_word_list)):
                if rep_word == text_word_list[word_index]:
                    text_word_list[word_index] = pla_word
            text[line_index] = " ".join(text_word_list)

        text = text_state(text)
        print_text(text)
    elif operation == 6:
        # 6) Вычисление арифметических операции сложения и вычитания
        expressions = []

        for text_line in text:
            search = re.search(r"[+-]?[ ]*(\d*\.?\d+([eE][+-]?\d+)?)([ ]*[+-][ ]*(\d*\.?\d+([eE][+-]?\d+)?))+",
                               text_line)
            if search:
                expression = search.group().replace(" ", "")
                answer = 0

                while True:
                    expression_search = re.search(r"[+-]?\d*\.?\d+([eE][+-]?\d+)?", expression)
                    if expression_search:
                        expression = expression[len(expression_search.group()):]
                        answer += float(expression_search.group())
                    else:
                        break

                expressions.append(f"{search.group().replace(' ', '')}={answer}")

        if expressions:
            print(f"\nНайденные в тексте выражения и их решения:")
            print("\n".join(expressions), end="\n\n")
        else:
            print("\nВ тексте нет арифметичеких выражений\n")
    elif operation == 7:
        # 7) Найти предложение, в котором количество слов, содержащих каждую букву 2 и более раз, максимально
        text_word_list = []
        for text_line in text:
            for line_word in split_line(text_line):
                text_word_list.append(line_word)

        sentences = " ".join(text_word_list).split(".")[:-1]

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
