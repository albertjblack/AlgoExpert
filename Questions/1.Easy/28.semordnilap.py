def semordnilap(words):
    # based on a list of unique words, return a list of semordnilap pairs
    result = []

    words_set = set(words)

    for word in words:
        reversed = word[::-1]
        if reversed in words_set and reversed != word:
            result.append([word, reversed])

    return result
