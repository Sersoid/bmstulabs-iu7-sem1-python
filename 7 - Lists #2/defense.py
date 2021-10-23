def check(raw_input):
    if raw_input:
        if raw_input[0] == "e" and not raw_input[1:].isdigit() or \
                raw_input[-1] == "e" and not raw_input[:-1].isdigit():
            return None
        else:
            processed_input = raw_input.replace("+", "", 1).replace("-", "", 1).replace("e", "", 1).replace(".", "", 1)
            if processed_input.isdigit():
                if raw_input[0] == "e" and raw_input[1:].isdigit():
                    return float(raw_input[1:])
                elif raw_input[-1] == "e" and raw_input[:-1].isdigit():
                    return float(raw_input[:-1])
                else:
                    return float(raw_input)
            else:
                return None
    else:
        return None


n = int(input("Введите кол-во строк, которое собираетесь вводить: "))

result = []

for i in range(n):
    string = input(f"{i + 1}> ")
    string_parts = []
    new_string = ""
    for char in string:
        if char in ("-", "+", ".", "e", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            new_string += char
        elif new_string:
            string_parts.append(new_string)
            new_string = ""

    if new_string:
        string_parts.append(new_string)

    # print(string_parts)

    for elem in string_parts:
        new_elem = check(elem)
        if new_elem:
            result.append(new_elem)

print(f"\nВсе найденные числа:\n{result}")
