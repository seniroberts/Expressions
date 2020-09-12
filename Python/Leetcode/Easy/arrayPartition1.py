"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n 
as large as possible.

Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4)

"""


def arrayPartition(an_array):
    an_array.sort()
    num_sum = 0

    for i in range(0, len(an_array), 2):
        num_sum += an_array[i]
    return num_sum


print("1st Approach-->", arrayPartition([1, 4, 3, 2]))


def arrayPairSum(an_array):
    return sum([i for i in sorted(an_array)[::2]])


print("2nd Approach-->", arrayPairSum([1, 4, 3, 2]))
