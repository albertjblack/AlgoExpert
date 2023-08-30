def twoNumberSum1(array, targetSum):
    hash_set = set()
    for i in range(len(array)):
        hash_set.add(array[i])

    for val in hash_set:
        if (targetSum - val in hash_set) and (targetSum - val != val):
            return [val, targetSum - val]

    return []


def twoNumberSum2(array, targetSum):
    hash_map = {}
    for e in array:
        if e in hash_map:
            pass
        else:
            hash_map[e] = targetSum - e

    for k, v in hash_map.items():
        if (k + v == targetSum) and (k != v) and (v in hash_map):
            return [k, v]

    return []


def twoNumberSum3(array, targetSum):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []


if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

    result1 = twoNumberSum1(array, targetSum)
    assert result1 == [11, -1]

    result2 = twoNumberSum2(array, targetSum)
    assert result2 == [11, -1]

    result3 = twoNumberSum3(array, targetSum)
    assert result3 == [11, -1]
