def count_nucleotides(dna):
    """
    Counts and returns the number of occurrences of each nucleotide in a DNA string.
    """
    return "".join(str(dna.count(nuc))+" " for nuc in "ACGT")
