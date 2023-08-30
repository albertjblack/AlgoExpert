def firstNonRepeatingCharacter(string):
    # find the first non repeating character and return its index or -1 if not a single option
    if len(string) < 1:
        return -1

    letter_to_idx_count = {}
    for idx in range(len(string)):
        if string[idx] not in letter_to_idx_count:
            letter_to_idx_count[string[idx]] = [idx, 1]
        else:
            letter_to_idx_count[string[idx]][1] += 1

    index_of_first = len(string) - 1
    has_unique = False
    for key, val in letter_to_idx_count.items():
        if val[0] <= index_of_first and val[1] == 1:
            index_of_first = val[0]
            has_unique = True

    return index_of_first if has_unique else -1
