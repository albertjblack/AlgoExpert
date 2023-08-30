def findThreeLargest(arr):
    result = [float("-inf")] * 3

    for num in arr:
        if num > arr[2]:
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = num

        elif num > arr[1]:
            arr[0] = arr[1]
            arr[1] = num

        elif num > arr[0]:
            arr[0] = num

    return result
