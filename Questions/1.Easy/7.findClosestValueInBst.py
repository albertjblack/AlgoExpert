def findClosestValueInBst(tree, target):
    # Write your code here.
    difference = float("inf")
    closest = float("inf")

    queue = [tree]
    while len(queue) > 0:
        curr = queue.pop(0)
        new_diff = abs(target - curr.value)

        if new_diff < difference:
            closest = curr.value
            difference = new_diff

        if curr.value < target:
            # do not add smaller numbers -> greater difference
            if curr.right != None:
                queue.append(curr.right)

        if curr.value > target:
            # just add the left, might be closer
            if curr.left != None:
                queue.append(curr.left)

    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(my_dict):
    database = {}
    root_id = None

    for node_entry in my_dict["tree"]["nodes"]:
        if root_id == None:
            root_id = node_entry["id"]
        database[node_entry["id"]] = BST(node_entry["value"])

    current = None
    for node_entry in my_dict["tree"]["nodes"]:
        current = database[node_entry["id"]]

        if node_entry["left"] != None:
            current.left = database[node_entry["left"]]
        if node_entry["right"] != None:
            current.right = database[node_entry["right"]]

    return database[root_id]


def in_order(root):
    if root == None:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)


if __name__ == "__main__":
    my_dict = {
        "target": 12,
        "tree": {
            "nodes": [
                {"id": "10", "left": "5", "right": "15", "value": 10},
                {"id": "15", "left": "13", "right": "22", "value": 15},
                {"id": "22", "left": None, "right": None, "value": 22},
                {"id": "13", "left": None, "right": "14", "value": 13},
                {"id": "14", "left": None, "right": None, "value": 14},
                {"id": "5", "left": "2", "right": "5-2", "value": 5},
                {"id": "5-2", "left": None, "right": None, "value": 5},
                {"id": "2", "left": "1", "right": None, "value": 2},
                {"id": "1", "left": None, "right": None, "value": 1},
            ],
            "root": "10",
        },
    }
    root = build_tree(my_dict)
    # in_order(root)

    target = 12
    closest = findClosestValueInBst(root, target)
    print(closest)
