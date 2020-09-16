"""
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie. Each child i has a greed factor gi,
which is the minimum size of a cookie that the child will be content with;
and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the
child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the
maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:
Input: [1,2], [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.

"""


def assignCookies(array1, array2):
    list_diff = len(set(
        [i for i in array1 + array2 if i in array1 and i in array2]))
    return list_diff


# print(assignCookies([1, 2, 30], [20, 10]))
# print(assignCookies([1, 2, 3], [1, 1]))
# print(assignCookies([1, 2], [1, 2, 3]))


def cookieDistributor(greedFactor, cookieArray):
    cookie_counter = 0
    for value in greedFactor:
        if value in cookieArray:
            cookieArray.remove(value)
            cookie_counter += 1
        else:
            leftOver = [i for i in cookieArray if i >= value]
            if leftOver:
                cookieArray.remove(min(leftOver))
                cookie_counter += 1
    return cookie_counter


print(cookieDistributor([10], [1]))
print(cookieDistributor([1, 2, 3], [1, 1]))
print(cookieDistributor([1, 2], [1, 2, 3]))
