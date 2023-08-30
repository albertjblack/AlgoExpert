def runLengthEncoding(string):
    result = ""
    l = 0
    r = 0
    count = 0

    while r < len(string):
        while (
            r < len(string) and l < len(string) and string[l] == string[r] and count < 9
        ):
            count += 1
            r += 1
        result += str(count)
        result += string[l]
        l = r
        count = 0

    return result
