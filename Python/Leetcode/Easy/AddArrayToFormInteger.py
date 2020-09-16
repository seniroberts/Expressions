"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

"""


def makeArray(nums, value):
    arraySum = 0
    for digit in nums:
        arraySum = 10 * arraySum + digit
    arrayPlusValue = str(arraySum + value)

    finalArray = [int(i) for i in arrayPlusValue]
    return finalArray


print(makeArray([1, 2, 0, 0], 34))
print(makeArray([2, 1, 5], 806))
