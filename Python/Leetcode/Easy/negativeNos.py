"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1

"""


def countNegatives(nested_list):
    counter = 0
    for lists in nested_list:
        for numbers in lists:
            if numbers < 0:
                counter += 1
    return counter


def test():
    nested_list = [[4, 3, 2, -1], [3, 2, 1, -1],
                   [1, 1, -1, -2], [-1, -1, -2, -3]]
    nested_list2 = [[3, 2], [1, 0]]
    nested_list3 = [[1, -1], [-1, -1]]
    nested_list4 = [[-1]]

    print(nested_list, "negative count-->", countNegatives(nested_list))
    print(nested_list2, "negative count-->", countNegatives(nested_list2))
    print(nested_list3, "negative count-->", countNegatives(nested_list3))
    print(nested_list4, "negative count-->", countNegatives(nested_list4))


test()


def countNegatives2(nested_list):
    return len([numbers for lists in nested_list for numbers in lists if numbers < 0])


print(countNegatives2([[4, 3, 2, -1], [3, 2, 1, -1],
                       [1, 1, -1, -2], [-1, -1, -2, -3]]))
