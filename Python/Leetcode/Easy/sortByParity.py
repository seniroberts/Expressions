"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted
"""


def sortByParity1(an_array):
    evenList = []
    oddList = []

    for i in range(len(an_array)):
        if an_array[i] % 2 == 0:
            evenList.append(an_array[i])
        else:
            oddList.append(an_array[i])
    evenList.extend(oddList)
    return evenList


def test():
    original_array = [3, 1, 2, 4]
    print("Original Array-->", original_array)
    print("Sorted by parity:--->", sortByParity1(original_array))


test()


def sortByParity2(an_array):
    return [i for i in an_array if i % 2 == 0] + [i for i in an_array if i % 2 != 0]


def test():
    original_array = [3, 1, 2, 4]
    print("Original Array-->", original_array)
    print("Sorted by parity2:--->", sortByParity2(original_array))


test()
