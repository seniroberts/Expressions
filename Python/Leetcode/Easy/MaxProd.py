"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
"""


def MaxProduct(an_array):
    left_side = max(an_array) - 1
    an_array.remove(max(an_array))

    right_side = max(an_array) - 1
    return left_side * right_side


def test():
    input_array = [3, 4, 5, 2]
    input_array2 = [1, 5, 4, 5]
    input_array3 = [3, 7]

    print("testcase1-->", MaxProduct(input_array))
    print("testcase2-->", MaxProduct(input_array2))
    print("testcase3-->", MaxProduct(input_array3))


test()
