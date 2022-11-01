from Bio import SeqIO

sequence =  SeqIO.parse("reference.fasta", "fasta")
seq = next(sequence)
print("Length of reference sequence is > " + str(len(seq)))


sequences = SeqIO.parse("reads.fasta", "fasta") 
reads_len = 0
for read in sequences:
    reads_len += len(read)

print("Length of combined sequence of the reads is > " + str(reads_len))

coverage = reads_len / len(seq)
print("Coverage of the given dataset is > " + str(coverage))