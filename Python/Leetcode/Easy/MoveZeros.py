"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


def moveZeros(nums):
    i = 0
    zeros = 0
    while i < len(nums) - zeros:
        if nums[i] == 0:
            zeros += 1
            nums.pop(i)
            print("popped", i)
            # print(nums)
            nums.append(0)
        else:
            i += 1
    return nums


print(moveZeros([0, 1, 0, 3, 12]))
print(moveZeros([0, 0, 1]))
