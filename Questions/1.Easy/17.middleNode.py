# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
ASSUME
- 1+ nodes
- return middle node
- if even length 1 2 2 4 -> return second node
MATH 
- len(ll) % 2 == 0
-- return at len/2 + 1
- len % 2 != 0
-- return at int(len/2) + 1
"""


def middleNode(linkedList):
    # Write your code here.
    # get length
    if linkedList.next == None:
        return linkedList

    curr = linkedList
    node_count = 0

    while curr:
        node_count += 1
        curr = curr.next

    # mid for even is exact, mid for odd is undercounted by 1
    # since returning the next node for the even, then this works on odd
    middle_node_position = int(node_count / 2)

    curr = linkedList
    current_pos = 1

    while current_pos != middle_node_position:
        curr = curr.next
        current_pos += 1

    return curr.next
