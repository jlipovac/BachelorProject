from Bio import SeqIO


n = 0
length_sum = 0

sequence = SeqIO.parse("A.fasta", "fasta")
seq = next(sequence)
shortest = len(seq)

for read in SeqIO.parse("A.fasta", "fasta"):
    n += 1
    length_sum += len(read)
    shortest = min(shortest, len(read))


print("Size of the shortest read in the file is > " + str(shortest))
print("File contains " + str(n) + " reads.")
print("Average length of a read is > " + str(round(length_sum/n, 2)))
