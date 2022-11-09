from Bio import SeqIO
import argparse
from utils import ends_with

parser = argparse.ArgumentParser(
    prog='Assignment 1',
    description='Modifies the input .fasta file so that the heder contains the length of a read instead of the end index',
    epilog='some text')
parser.add_argument("input", help="Input file path containing reads, must be in fasta format")
parser.add_argument("output", help="Output file path, can be an inexistent file in which case it is created, must be in fasta format")
args = parser.parse_args()
extensions = ['.fasta', '.fna', '.ffn', '.faa', '.frn', '.fa']

if ends_with(args.input, extensions):
    raise ValueError('File should be in fasta format')
if ends_with(args.output, extensions):
    raise ValueError('File should be in fasta format')

sequences = list()
for record in SeqIO.parse(args.input, "fasta"):
    id_B_S, E = record.description.split("end=")
    record.description = id_B_S + "length=" + str(len(record.seq))
    sequences.append(record)

with open(args.output, "w") as output_handle:
    SeqIO.write(sequences, output_handle, "fasta")
