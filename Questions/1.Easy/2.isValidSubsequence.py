"""
Not necessarily adjacent
subsequence -> same order
"""


def isValidSubsequence(array, sequence):
    if len(array) == 0 or len(sequence) == 0:
        return False

    arr_ptr = 0
    seq_ptr = 0

    while seq_ptr != len(sequence) and arr_ptr != len(array):
        if sequence[seq_ptr] == array[arr_ptr]:
            seq_ptr += 1
            arr_ptr += 1
        else:
            arr_ptr += 1

    if seq_ptr != len(sequence):
        return False
    return True


if __name__ == "__main__":
    arr = [5, 1, 22, 25, 6, -1, 8, 10]
    seq = [1, 6, -1, 10]

    assert isValidSubsequence(arr, seq) == True
