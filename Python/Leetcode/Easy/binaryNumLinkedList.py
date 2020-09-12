"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.


Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0
"""

"""
1011 base 2 to base 10

1 * 2^0
1 * 2^1
0 * 2^2
1 * 1^3
==========> 11


101 ---> base 10
1 * 2^0
0 * 2^1
1 * 2^2

======> 5
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        output = "["
        current_node = self.head
        while current_node:
            output += str(current_node.value) + "-->"
            current_node = current_node.next_node
        output += "]"
        return output

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def getDecimalValue(self, value):
        listOfValues = []
        current_node = self.head
        total_sum = 0
        while current_node:
            listOfValues.append(current_node.value)
            current_node = current_node.next_node

        reverse_index = len(listOfValues) - 1
        for num in listOfValues:
            total_sum += num * (2 ** reverse_index)
            reverse_index -= 1
        return total_sum


def listBuilder(a_list):
    dummy_list = LinkedList()
    for i in a_list:
        dummy_list.append(i)
    return dummy_list


test = listBuilder([1, 0, 1])
print(test)
print(test.getDecimalValue(1))
