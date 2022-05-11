def reverse_complement(s):
    """
    Returns the reverse complement of a DNA string.
    """
    return s[::-1].replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper()
