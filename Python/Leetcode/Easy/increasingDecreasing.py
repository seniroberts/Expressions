"""
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

 
Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm
"""


def sortString(input_string):
    result = ""
    blank = ""

    while input_string:
        sorted_input_string = sorted(set(input_string))
        result += "".join(sorted_input_string)

        for character in sorted_input_string:
            input_string = input_string.replace(character, blank, 1)

        reversed_sorted_input_string = sorted(set(input_string), reverse=True)
        result += "".join(reversed_sorted_input_string)
        for character in sorted_input_string:
            input_string = input_string.replace(character, blank, 1)
    return "".join(result)


def test():
    input1 = "aaaabbbbcccc"
    input2 = "rat"
    input3 = "leetcode"
    input4 = "spo"
    print(input1, "--->", sortString(input1))
    print(input2, "--->", sortString(input2))
    print(input3, "--->", sortString(input3))
    print(input4, "--->", sortString(input4))


test()
