"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed
"""


def num_identical_pairs(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print(nums[j], nums[i])
            if nums[i] == nums[j] and i < j:
                result += 1
    return result


print(num_identical_pairs([1, 1, 1, 1]))


def num_identical_pairs2(nums):
    num_dict = {}
    freq = 0
    for num in nums:
        if num in num_dict:
            freq += num_dict[num]
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return freq


print(num_identical_pairs2([1, 1, 1, 1]))
