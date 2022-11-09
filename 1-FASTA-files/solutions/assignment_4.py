from Bio import SeqIO
import argparse
from utils import add_reads

parser = argparse.ArgumentParser(
    prog='Assignment 4',
    description='From the file \"A.fasta\" created as described in \"Assignment 3\", this computes the length of the '
                'shortest read in the file, the total number of reads and the average length of a read.')
args = add_reads(parser)

shortest = float('inf')
avg_length = 0
num_sequences = 0
for record in SeqIO.parse(args.reads, "fasta"):
    if len(record.seq) < shortest:
        shortest = len(record.seq)
    num_sequences += 1
    avg_length += len(record.seq)

avg_length /= num_sequences
print("The shortest read in the file is " + str(shortest) + " bases long.")
print("There are " + str(num_sequences) + " reads in the file.")
print("The average length of a read is " + str(avg_length) + " bases.")

