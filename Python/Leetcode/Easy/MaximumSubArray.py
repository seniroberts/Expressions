"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6
https://leetcode.com/problems/maximum-subarray/
"""


def MaxSubArray(nums):
    currentMax = 0
    bestMax = 0

    for num in nums:
        currentMax = max(currentMax + num, num)
        bestMax = max(currentMax, bestMax)

    return bestMax


print(MaxSubArray([-2, 1]))
