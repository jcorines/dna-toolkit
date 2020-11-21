# main.py
from DNAToolkit import *
import random

rndDNAstr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])
DNAstr = validateSeq(rndDNAstr)
print(countNucFrequency(rndDNAstr))
