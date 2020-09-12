"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""

# 1st Approach:


def SortByParity(an_array):
    oddList = []
    evenList = []
    result = []

    for i in range(len(an_array)):
        if an_array[i] % 2 == 0:
            evenList.append(an_array[i])
        else:
            oddList.append(an_array[i])

    for i in range(len(evenList)):
        result.append(evenList[i])
        result.append(oddList[i])
    return result


def test():
    theArray = [4, 2, 5, 7]
    theArray2 = [3, 6, 8, 7, 9, 2]
    print("Original Array:--->", theArray)
    print("Array Sorted by Parity:--->", SortByParity(theArray))
    print("Array Sorted by Parity:--->", SortByParity(theArray2))


test()


# 2nd Approach

def SortByParity2(an_array):
    new_array = [0] * len(an_array)
    print(new_array)

    even_pointer = 0
    odd_pointer = 1

    for i in an_array:
        if i % 2 == 0:
            new_array[even_pointer] = i
            print("Even Array", new_array)
            even_pointer += 2
        else:
            new_array[odd_pointer] = i
            odd_pointer += 2
    return new_array


print(SortByParity2([4, 2, 5, 7]))
