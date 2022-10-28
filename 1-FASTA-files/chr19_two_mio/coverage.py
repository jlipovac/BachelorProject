from Bio import SeqIO
d = 0
for record in SeqIO.parse("reference.fasta", "fasta"):
    d = len(record.seq)
    print("Length of the reference sequence is ->", d)
zbroj = 0
for record in SeqIO.parse("reads.fasta", "fasta"):
    zbroj += len(record.seq)
print("Length of the combined sequence of the reads is ->", zbroj)
print("Coverage is ->", zbroj/d)