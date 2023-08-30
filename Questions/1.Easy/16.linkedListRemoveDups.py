# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    if linkedList == None:
        return None

    # current is updated only when breaking out of inner loop check
    # what gets updated in inner loop is the next node to current

    curr = linkedList
    while curr:
        while curr.next and curr.next.value == curr.value:
            curr.next = curr.next.next
        curr = curr.next

    return linkedList
