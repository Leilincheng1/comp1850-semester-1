# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
# """
#     This task assumes some experience with Python.
#
#     You are given incomplete function valid_char_in_string with a docstring.
#     Your task is to complete the function based on the details in the
#     docstring.
# """
#
#
# def valid_char_in_string(popList, charSet):
#     """
#     This function takes two arguments popList and charSet, in which popList
#     is a list of strings and charSet is a list of strings with a length of 1
#     (a character).
#
#     This function returns a Boolean False if any string in popList contains
#     characters not in charSet, or invalid charSet. Otherwise, returns
#     a Boolean True. Examples of valid charSet are ['0', '1'], ['-', '*'].
#     """
#
# test data
#
# plist1 = ['00000', '00001', '00010', '00011', '00100']
# charset1 = ['0', '1']
# print(valid_char_in_string(plist1, charset1))  # True
#
# plist2 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc', 'tcg',
#           'ccg', 'cca', 'ata']
# charset2 = ['a', 'c', 't', 'g']
# print(valid_char_in_string(plist2, charset2))  # True
#
# plist3 = ['aac', 'ctt', 'gat', 'ccc', 'gcc', 'ctg', 'gtc']
# charset3 = ['a', 'c']
# print(valid_char_in_string(plist3, charset3))  # False
#
# plist4 = ['00000', '00001', '00010', '00011', '00100']
# charset4 = '01'
# print(valid_char_in_string(plist4, charset4))  # False
# ============================================================================
# Completed solution
# ============================================================================
"""Check that all strings contain only characters in a valid character list."""


def valid_char_in_string(popList, charSet):
    """Return False for invalid character sets or disallowed input characters."""
    if (not isinstance(charSet, list) or not charSet or
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
