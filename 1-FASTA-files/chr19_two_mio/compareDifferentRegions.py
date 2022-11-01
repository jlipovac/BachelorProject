from Bio import SeqIO

sequencesA = []
sequencesB = []
i = 0
j = 0
lenA = 0
lenB = 0
for read in SeqIO.parse("reads.fasta", "fasta"):
    start = int((((read.description.split("="))[2]).split(",")[0]))

    if(start >= 500000 and start <= 600000):
        i += 1
        read.id = str(i)
        desc = read.description.split(" ", 1)[1]
        read.description = read.id + " " + desc
        sequencesA.append(read)
        lenA += len(read)

    elif(start >= 1500000 and start <= 1600000):
        j += 1
        read.id = str(j)
        desc = read.description.split(" ", 1)[1]
        read.description =  read.id + " " + desc
        sequencesB.append(read)
        lenB += len(read)

SeqIO.write(sequencesA, "A.fasta", "fasta")
SeqIO.write(sequencesB, "B.fasta", "fasta")

sequence =  SeqIO.parse("reference.fasta", "fasta")
seq = next(sequence)

print("Coverage of read set A is > " + str(lenA/len(seq)))
print("Coverage of read set b is > " + str(lenB/len(seq)))
print("The results are similar because the sequences were taken from ranges of same size.")