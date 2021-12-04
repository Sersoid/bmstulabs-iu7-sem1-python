text = [
    "Он благополучно избегнул встречи с своею хозяйкой на лестнице. Каморка его приходилась под самою кровлей высокого",
    "пятиэтажного дома и походила более на шкаф, чем на квартиру. Квартирная же хозяйка его, у которой он нанимал",
    "эту каморку с обедом и прислугой, помещалась одною лестницей ниже, в отдельной квартире, и каждый раз, при выходе",
    "на улицу, 3 - 2 - 1 ему непременно надо было проходить мимо хозяйкиной кухни, почти всегда настежь отворенной на",
    "два слова",
    "лестницу. И каждый раз молодой человек, проходя мимо, чувствовал какое-то болезненное и трусливое ощущение,",
    "которого",
    "стыдился и от которого морщился. Он был 1-2-3 должен кругом хозяйке и боялся с нею встретиться."
]

result_index = 0
result_count = 0

for line_index in range(len(text)):
    max_count = 0
    current_count = 0
    current_len = 0

    for word in text[line_index].split():
        word_len = len(word)
        if word_len > current_len:
            current_count += 1
        else:
            max_count = current_count
            current_count = 1
        current_len = word_len

    if result_count < max_count:
        result_count = max_count
        result_index = line_index

print(text[result_index])
