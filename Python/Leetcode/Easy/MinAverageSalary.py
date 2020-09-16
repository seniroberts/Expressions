"""
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500

"""


def AverageSalary(array):
    max_value = max(array)
    min_value = min(array)
    array.remove(max_value)
    array.remove(min_value)
    array_length = len(array)
    return sum(array)/array_length


print(AverageSalary([4000, 3000, 1000, 2000]))
print(AverageSalary([3000, 1000, 2000]))


def Average2(array):
    max_value = max(array)
    min_value = min(array)

    freshArray = []
    for i in range(len(array)):
        if array[i] != max_value and array[i] != min_value:
            freshArray.append(array[i])
    return sum(freshArray)/len(freshArray)


print("Option 2--->", Average2([3000, 1000, 2000]))
print("Option 2--->", Average2([4000, 3000, 1000, 2000]))
