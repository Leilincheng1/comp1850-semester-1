"""Check that all strings contain only characters in a valid character list."""


def valid_char_in_string(popList, charSet):
    """Return False for invalid character sets or disallowed input characters."""
    if (not isinstance(charSet, list) or
            any(not isinstance(c, str) or len(c) != 1 for c in charSet)):
        return False
    if not isinstance(popList, list) or any(not isinstance(s, str) for s in popList):
        return False
    return all(character in charSet for word in popList for character in word)


if __name__ == "__main__":
    print(valid_char_in_string(["00000", "00100"], ["0", "1"]))
    print(valid_char_in_string(["aac", "gtc"], ["a", "c", "t", "g"]))
    print(valid_char_in_string(["aac", "gtc"], ["a", "c"]))
    print(valid_char_in_string(["00000"], "01"))
