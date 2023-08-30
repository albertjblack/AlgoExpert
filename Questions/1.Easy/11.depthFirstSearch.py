# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        # array is the array to be returned
        stack = [self]  # starts with the first node where the dfs was called
        while len(stack) > 0:
            curr = stack.pop(-1)
            array.append(curr.name)
            for i in range(len(curr.children) - 1, -1, -1):
                stack.append(curr.children[i])
        return array
