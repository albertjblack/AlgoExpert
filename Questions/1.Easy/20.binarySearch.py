def binarySearch(arr, tgt):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = int((l + r) / 2)

        if arr[m] == tgt:
            return m

        elif arr[m] > tgt:
            r = m - 1

        elif arr[m] < tgt:
            l = m + 1

    return -1
