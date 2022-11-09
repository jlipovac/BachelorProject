from Bio import SeqIO
import argparse
from utils import add_reference_and_reads

parser = argparse.ArgumentParser(
    prog='Assignment 2',
    description='Computes the length of the reference sequence, as well as the length of the combined sequence of the reads and the coverage',
    epilog='some text')
args = add_reference_and_reads(parser)

len_reference = 0
for record in SeqIO.parse(args.reference, "fasta"):
    print("Length of the reference sequence: " + str(len(record.seq)))
    len_reference = len(record.seq)

len_combined = 0
for record in SeqIO.parse(args.reads, "fasta"):
    len_combined += len(record.seq)
print("Length of the combined sequence of the reads: " + str(len_combined))

print("Coverage of the given dataset: " + str(len_combined / len_reference))
