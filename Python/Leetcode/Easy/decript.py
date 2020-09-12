import string


def frequentAlphabet(input_string):
    input_string.split("#")

    alphabets = [i for i in string.ascii_lowercase]
    hashSign = "#"

    oneToNine = [str(i) for i in list(range(1, 10))]
    tenAbove = [str(i) for i in list(range(10, 27))]

    tenAbove_with_hashsign = []
    for i in range(len(tenAbove)):
        tenAbove[i] += hashSign
        tenAbove_with_hashsign.append(tenAbove[i])

    numList = oneToNine + tenAbove_with_hashsign

    alpha_num_map = {key: value for key, value in zip(numList, alphabets)}

    result = {}
    for key, value in alpha_num_map.items():
        for i in input_string:
            if i == key:
                result[key] = value
            return result


#     # character_map = {}
# print(frequentAlphabet("10#11#12"))

# # print(list(range(10, 27)))


# text = "10#11#12"
# print(text.split("#"))
# # print(text)


# champ_ids = [10, 11, 1, 2]
# champ_dict = {'a': 10, 'b': 11, 'c': 5, 'd': 1, 'e': 2}
# result = [k for k, v in champ_dict.items() if v in champ_ids]

# print(result)

# print(champ_ids)


def freqAlphabets(s):
    r = ""
    i = 0
    while i < len(s):
        if s[-i-1] == '#':
            t = int(s[-i-3:-i-1])
            print("T-->", t)
            r += chr(ord('a')+t-1)
            print("R-->", r)
            i += 2
        else:
            r += chr(ord('a') + int(s[-i-1])-1)
            print("R2-->", r)
        i += 1

    return r[::-1]


print(freqAlphabets("10#11#12"))
