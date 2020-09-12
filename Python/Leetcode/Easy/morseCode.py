"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

"""
import string


def UniqueMorseRepresentations(an_array):

    alphabet_import = string.ascii_lowercase
    alphabets = [i for i in alphabet_import]
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
    return len(unique_values)


def test():
    input_words = ["gin", "zen", "gig", "msg"]
    print("Input:", input_words)
    print("No of Transformations: ", UniqueMorseRepresentations(input_words))


test()


# def UniqueMorseRepresentations(an_array):

#     alphabet_import = string.ascii_lowercase
#     alphabets = [i for i in alphabet_import]
#     morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
#                   "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

#     alphabet_code_map = {key: value for key,
#                          value in zip(alphabets, morse_code)}

#     transformed_words = ""

#     for words in an_array:
#         for letters in words:
#             transformed_words += alphabet_code_map[letters]
#     return len(set(transformed_words))


# def test():
#     input_words = ["gin", "zen", "gig", "msg"]
#     print("Input:", input_words)
#     print("No of Transformations: ", UniqueMorseRepresentations(input_words))


# test()
