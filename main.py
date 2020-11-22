# main.py
from DNAToolkit import *
from utilities import colored
import random


rndDNAstr = "".join([random.choice(Nucleotides) for nuc in range(50)])
DNAstr = validateSeq(rndDNAstr)
print(countNucFrequency(rndDNAstr))
print(transcription(DNAstr))

tmpStr = "TEST"
print(DNAstr)
print(reverse_complement(DNAstr))

print(f"{gc_count(DNAstr)}")

print(f"{gc_content_subsec(DNAstr, k=5)}")
