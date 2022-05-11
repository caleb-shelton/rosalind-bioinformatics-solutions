def hamming_distance(str1, str2):
    """
    Calculate the Hamming distance between two strings.
    """
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length.")
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))
