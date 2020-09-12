import string
import re


# def mostCommonWord(sentence, bannedWord):
#     sentence = sentence.lower().strip().replace(".", "").replace(",", "").split()
#     specialCharacters = [",", ".", "#", "@", "!", "/", ""]
#     freq_map = {}

#     for word in sentence:
#         if word not in bannedWord:
#             if word in freq_map:
#                 freq_map[word] += 1
#             else:
#                 freq_map[word] = 1
#     # clean_dict = {key: value for key,
#     #               value in freq_map.items() if key != bannedWord}
#     return max(freq_map, key=freq_map.get)


# print("Most Common Word is:", mostCommonWord(
#     "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))


# aaa = "Bob hit a ball::>?<%$#@!, the ^%| BALL$ flew# far after@ it was hit."

# print(re.split("\W+", aaa))


an_array = ["gin", "zen", "gig", "msg"]
morse_words = ""

extract_alphabet = string.ascii_lowercase
alphabets = [i for i in extract_alphabet]
morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
              "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

alphabet_code_map = {key: value for key,
                     value in zip(alphabets, morse_code)}

transformed_words = ""
transformed_word_map = {}

for words in an_array:
    for letters in words:
        transformed_words += alphabet_code_map[letters]

    transformed_word_map[words] = transformed_words
    transformed_words = ""

unique_values = set(transformed_word_map.values())
print(len(unique_values))
