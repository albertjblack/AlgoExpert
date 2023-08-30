def caesarCipherEncryptor(string, key):
    if len(string) == 0:
        return ""
    if key < 0:
        return string

    new_string = ""
    for char in string:
        # based on a, subtract the char and add shift to then mod up
        if char.islower():
            # 97 - 100
            new_char = chr(((ord(char) - ord("a") + key) % 26) + ord("a"))
            new_string += new_char
        else:
            new_string += char

    return new_string
