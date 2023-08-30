def generateDocument(characters, document):
    # return True or False depending if the document can be formed with the available characters
    if document == "":
        return True

    letter_to_count = {}
    for char in characters:
        if char not in letter_to_count:
            letter_to_count[char] = 1
        else:
            letter_to_count[char] += 1

    for char in document:
        if char in letter_to_count:
            if letter_to_count[char] > 0:
                letter_to_count[char] -= 1
            else:
                return False
        else:
            return False

    return True
