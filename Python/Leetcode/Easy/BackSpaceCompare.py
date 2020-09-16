"""
Given two strings S and T, return if they are equal when both are typed into 
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

"""


def BackSpaceCompare(word1, word2):
    def compareword(word):
        while "#" in word:
            wordIndex = word.index("#")
            if wordIndex == 0:
                word = word[1:]
            else:
                word = word[:wordIndex-1] + word[wordIndex+1:]
        return word

    return compareword(word1) == compareword(word2)


# print(BackSpaceCompare("ab#c", "ad#c"))
# print(BackSpaceCompare("ab##", "c#d#"))


def BackSpaceCompare(word1, word2):
    def wordBuilder(word):
        finalArray = []
        for letter in word:
            if letter != "#":
                finalArray.append(letter)
            elif finalArray != None:
                finalArray.pop()
        return "".join(finalArray)
    return wordBuilder(word1) == wordBuilder(word2)


print(BackSpaceCompare("ab#c", "ad#c"))
