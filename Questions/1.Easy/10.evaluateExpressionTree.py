# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # we need the left and the right and then we operate on them based on our negative value
    if tree.value >= 0:
        return tree.value

    left = evaluateExpressionTree(tree.left)
    right = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return left + right
    elif tree.value == -2:
        return left - right
    elif tree.value == -3:
        return int(left / right)
    else:
        return left * right
