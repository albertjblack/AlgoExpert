def build_tree(my_dict):
    database = {}
    root_id = None

    for node_entry in my_dict["tree"]["nodes"]:
        if root_id == None:
            root_id = node_entry["id"]
        database[node_entry["id"]] = BT(node_entry["value"])

    current = None
    for node_entry in my_dict["tree"]["nodes"]:
        current = database[node_entry["id"]]

        if node_entry["left"] != None:
            current.left = database[node_entry["left"]]
        if node_entry["right"] != None:
            current.right = database[node_entry["right"]]

    return database[root_id]


class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodesDepth(root):
    aggregatedSum = 0
    stack = [(root, 0)]

    while len(stack) > 0:
        currNode, currDepth = stack.pop(-1)
        aggregatedSum += currDepth

        if currNode.right:
            stack.append((currNode.right, currDepth + 1))
        if currNode.left:
            stack.append((currNode.left, currDepth + 1))

    return aggregatedSum


if __name__ == "__main__":
    my_dict = {
        "tree": {
            "nodes": [
                {"id": "1", "left": "2", "right": "3", "value": 1},
                {"id": "2", "left": "4", "right": "5", "value": 2},
                {"id": "3", "left": "6", "right": "7", "value": 3},
                {"id": "4", "left": "8", "right": "9", "value": 4},
                {"id": "5", "left": None, "right": None, "value": 5},
                {"id": "6", "left": None, "right": None, "value": 6},
                {"id": "7", "left": None, "right": None, "value": 7},
                {"id": "8", "left": None, "right": None, "value": 8},
                {"id": "9", "left": None, "right": None, "value": 9},
            ],
            "root": "1",
        }
    }
    root = build_tree(my_dict)
    print(nodesDepth(root))
