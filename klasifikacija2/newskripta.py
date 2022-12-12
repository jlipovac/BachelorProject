from Bio import SeqIO

ulazna_datoteka = input("full path name of kraken.out file: ")

data = open(ulazna_datoteka, "r")
C = []
U = []
for l in data:
    if l.startswith("C"):
        contig = l.split("\t")[1]
        taxid = l.split("\t")[2].split("(")[1].split(" ")[1][:-1]
        if (contig, taxid) not in C:
            C.append((contig, taxid))
    elif l.startswith("U"):
        notclassified = l.split("\t")[1]
        if notclassified not in U:
            U.append(notclassified)
data.close()

x = open("classified", "w")
x.write(str(len(C))+"\n")
for a in range(len(C)):
    if a == len(C)-1:
        x.write(C[a][0]+" "+C[a][1])
    else:
        x.write(C[a][0]+" "+C[a][1]+"\n")
x.close()

y = open("unclassified", "w")
y.write(str(len(U))+"\n")
for b in range(len(U)):
    if b == len(U)-1:
        y.write(U[b])
    else:
        y.write(U[b]+"\n")
y.close()