from Bio import SeqIO

ulazna_datoteka1 = input("full path name of .fastq file: ")
ulazna_datoteka2 = input("full path name of kraken file: ")

d_fastq = {}
with open(ulazna_datoteka1) as f:
    for record in SeqIO.parse(f, "fastq"):
        id_reada = record.id
        naziv_bakterije = record.description.split(" ")[1].split(",")[0]
        d_fastq[id_reada] = naziv_bakterije
f.close()

file = open(ulazna_datoteka2)
d_kraken = {}
unclassified = []
for line in file:
    if line.startswith("C"):
        id = line.split("\t")[1]
        oznaka_krakena = line.split("\t")[2].split("(")[0][:-1]
        d_kraken[id] = naziv_bakterije
    elif line.startswith("U"):
        neklasificiran = line.split("\t")[1]
        if neklasificiran not in unclassified:
            unclassified.append(neklasificiran)
file.close()

br_tocnih = 0
krivi = []
for key, value in d_kraken.items():
    if value == d_fastq[key]:
        br_tocnih += 1
    else:
        krivi.append(key)
        
a = open("numberCorrect", "w")
a.write(str(br_tocnih))
a.close()
b = open("U", "w")
for i in range(len(unclassified)):
    if i == len(unclassified)-1:
        b.write(unclassified[i])
    else:
        b.write(unclassified[i]+"\n")
b.close()
c = open("wrongName", "w")
for j in range(len(krivi)):
    if j == len(krivi)-1:
        c.write(krivi[j])
    else:
        c.write(krivi[j]+"\n")
c.close()