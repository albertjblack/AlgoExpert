def transposeMatrix(matrix):
    # DIMENSIONS columns become rows and rows become columns
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    transposed = [[0 for i in range(n_rows)] for i in range(n_cols)]

    for col_idx in range(n_cols):
        for row_idx in range(n_rows):
            transposed[col_idx][row_idx] = matrix[row_idx][col_idx]

    return transposed


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    print(transposeMatrix(matrix))
