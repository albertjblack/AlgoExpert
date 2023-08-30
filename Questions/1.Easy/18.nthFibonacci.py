def getNthFib(n):
    # Write your code here.
    values = [-1] * max((n + 1), 3)

    values[0] = 0
    values[1] = 0
    values[2] = 1

    if n < 3 and n > -1:
        return values[n]

    position = 3
    while position <= n:
        values[position] = values[position - 1] + values[position - 2]
        position += 1

    return values[n]
