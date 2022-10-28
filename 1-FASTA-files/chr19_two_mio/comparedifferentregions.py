from Bio import SeqIO
i = 1
j = 1
A = []
B = []
for record in SeqIO.parse("reads.fasta", "fasta"):
    start = ((record.description.split(", "))[1].split('='))[1]
    if (int(start)>=500000 and int(start)<=600000):
        record.id = str(i)
        i += 1
        A.append(record)
    elif (int(start)>=1500000 and int(start)<=1600000):
        record.id = str(j)
        j += 1
        B.append(record)
SeqIO.write(A, "A.fasta", "fasta")
SeqIO.write(B, "B.fasta", "fasta")
ukupno = 0
for record in SeqIO.parse("reference.fasta", "fasta"):
    ukupno = len(record.seq)
zbrojA = 0
for record in SeqIO.parse("A.fasta", "fasta"):
    zbrojA += len(record.seq)
zbrojB = 0
for record in SeqIO.parse("B.fasta", "fasta"):
    zbrojB += len(record.seq)
print("Coverage of read set A is ->", zbrojA/ukupno)
print("Coverage of read set B is ->", zbrojB/ukupno)
print("The results are similar because the final amount of sequences is approximately the same in both observed regions.")