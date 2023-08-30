def commonCharacters(strings):
    # return common chars in all strings

    result = []
    letter_to_count = {}

    for string in strings:
        visited = set()
        for char in string:
            if char not in visited:
                if char not in letter_to_count:
                    letter_to_count[char] = 1
                else:
                    letter_to_count[char] += 1
                visited.add(char)

    for key, value in letter_to_count.items():
        if value == len(strings):
            result.append(key)

    return result
