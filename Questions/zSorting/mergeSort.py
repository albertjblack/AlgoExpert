def merge_sort(array):
    if len(array) > 1:
        left = array[: len(array) // 2]
        right = array[len(array) // 2 :]

        left = merge_sort(left)
        right = merge_sort(right)

        l = r = k = 0

        tmp = [0] * (len(left) + len(right))
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                tmp[k] = left[l]
                l += 1
            else:
                tmp[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            tmp[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            tmp[k] = right[r]
            r += 1
            k += 1
        return tmp
    return array


if __name__ == "__main__":
    arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 6]
    res = merge_sort(arr)
    print(res)
