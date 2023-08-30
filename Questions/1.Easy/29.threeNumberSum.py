def threeNumberSum(array, targetSum):
    # array of distinct integers
    # return ascending arrey of triplets adding to targetsum
    array.sort()
    result = []
    for i in range(len(array)):
        l = i + 1
        r = len(array) - 1
        while l < r:
            curr_sum = array[i] + array[l] + array[r]
            if curr_sum == targetSum:
                result.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif curr_sum < targetSum:
                l += 1
            else:  # greater than
                r -= 1
    return result
