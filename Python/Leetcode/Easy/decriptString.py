import string


def frequentAlphabets(input_string):
    string_store = []

    for character in range(0, len(input_string)):
        if input_string[character] == "#":
            character = string_store.pop()
            character2 = string_store.pop()
            string_builder = character2 + character
            string_store.append(string_builder)
        else:
            string_store.append(input_string[character])

    string_store = [int(i) for i in string_store]

    alphabets = [i for i in string.ascii_lowercase]
    numbers = [i for i in list(range(1, 27))]
    alpha_num_map = {key: value for key, value in zip(numbers, alphabets)}

    result = [alpha_num_map[num] for num in string_store]
    return "".join(result)


def test():
    input_string1 = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    input_string2 = "10#11#12"
    input_string3 = "25#"
    input_string4 = "1326#"

    print("Test1--->", frequentAlphabets(input_string1))
    print("Test2--->", frequentAlphabets(input_string2))
    print("Test3--->", frequentAlphabets(input_string3))
    print("Test4--->", frequentAlphabets(input_string4))


test()
