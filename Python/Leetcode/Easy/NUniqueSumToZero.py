"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]

"""


def SumZero(input_value):
    num_to_list = list(range(1, input_value))
    list_sum = sum(num_to_list)

    num_to_list.append(-sum(num_to_list))
    return num_to_list


print(SumZero(5))
