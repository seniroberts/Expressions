"""
Given two non-negative integers num1 and num2 represented as string, 
return the sum of num1 and num2.
Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

https://leetcode.com/problems/add-strings/
"""


def addStrings(num1, num2):
    num_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
               "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    num1_result = 0
    num2_result = 0
    for digit in num1:
        num1_result = 10 * num1_result + num_map[digit]
    for digit in num2:
        num2_result = 10 * num2_result + num_map[digit]
    return str(num1_result + num2_result)


print(addStrings("5", "5"))
