# DNA Toolkit file
import collections
from structures import *

Nucleotides = ["A", "C", "G", "T"]
DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

# Check the sequence to make sure it is a DNA String


def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict
    return dict(collections.Counter(seq))

    # return dict(collections.Counter(seq))


def transcription(seq):
    """ DNA -> RNA transcription"""
    return seq.replace("T", "U")


def reverse_complement(seq):
    """
    swapping adenine with thyrmine and guanine with cytosine
    Reversing generated string
    """
    return ''.join([DNA_ReverseComplement[nuc]for nuc in seq])[::-1]
    # mapping = str.maketrans('ATCG', 'TAGC')
    # return seq.translate(mapping)[::-1]


def gc_count(seq):
    """GC content is in a DNA/RNA sequce"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subsec(seq, k=20):
    """ GC content in a DNA/RNA sub-sequence k. k=20 by deault"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i: i + k]
        res.append(gc_count(subseq))
    return res
