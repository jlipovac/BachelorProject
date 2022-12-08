from Bio import SeqIO

ulazna_datoteka1 = input("full path name of .fastq file: ")
ulazna_datoteka2 = input("full path name of kraken file: ")
ulazna_datoteka3 = input("full path name of .txt file with taxids: ")

taxids = open(ulazna_datoteka3, "r")
lines = taxids.readlines()
tuples = {}
for row in lines:
    row = row.strip()
    ime = row.split(" ")[0]
    tax_id = row.split(" ")[1]
    tuples[ime] = tax_id

d_fastq = {}
with open(ulazna_datoteka1, "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        id_reada = record.id
        naziv_bakterije = record.description.split(" ")[1].split(",")[0]
        d_fastq[id_reada] = naziv_bakterije
f.close()

file = open(ulazna_datoteka2, "r")
d_kraken = {}
unclassified = []
for line in file:
    if line.startswith("C"):
        id = line.split("\t")[1]
        oznaka_krakena = line.split("\t")[2].split("(")[0][:-1]
        taxid = line.split("\t")[2].split("(")[1].split(" ")[1][:-1]
        d_kraken[id] = [naziv_bakterije, taxid]
    elif line.startswith("U"):
        neklasificiran = line.split("\t")[1]
        if neklasificiran not in unclassified:
            unclassified.append(neklasificiran)
file.close()

tocni_po_imenu = []
tocni_po_taxidu = []
krivi_po_imenu = []
krivi_po_taxidu = []
for key, value in d_kraken.items():
    if value[0] == d_fastq[key]:
        if key not in tocni_po_imenu:
            tocni_po_imenu.append(key)
    elif value[0] != d_fastq[key]:
        if key not in krivi_po_imenu:
            krivi_po_imenu.append(key)
    if value[1] == tuples[value[0]]:
        if key not in tocni_po_taxidu:
            tocni_po_taxidu.append(key)
    elif value[1] != tuples[value[0]]:
        if key not in krivi_po_taxidu:
            krivi_po_taxidu.append(key)
        
a = open("CorrectByName", "w")
a.write(str(len(tocni_po_imenu))+"\n")
for k in range(len(tocni_po_imenu)):
    if k == len(tocni_po_imenu)-1:
        a.write(tocni_po_imenu[k])
    else:
        a.write(tocni_po_imenu[k]+"\n")
a.close()

b = open("popis_neklasificiranih", "w")
b.write(str(len(unclassified))+"\n")
for i in range(len(unclassified)):
    if i == len(unclassified)-1:
        b.write(unclassified[i])
    else:
        b.write(unclassified[i]+"\n")
b.close()

c = open("WrongByName", "w")
c.write(str(len(krivi_po_imenu))+"\n")
for j in range(len(krivi_po_imenu)):
    if j == len(krivi_po_imenu)-1:
        c.write(krivi_po_imenu[j])
    else:
        c.write(krivi_po_imenu[j]+"\n")
c.close()

d = open("CorrectByTaxId", "w")
d.write(str(len(tocni_po_taxidu))+"\n")
for l in range(len(tocni_po_taxidu)):
    if l == len(tocni_po_taxidu)-1:
        d.write(tocni_po_taxidu[l])
    else:
        d.write(tocni_po_taxidu[l]+"\n")
d.close()

e = open("WrongByTaxId", "w")
e.write(str(len(krivi_po_taxidu))+"\n")
for m in range(len(krivi_po_taxidu)):
    if m == len(krivi_po_taxidu)-1:
        e.write(krivi_po_taxidu[m])
    else:
        e.write(krivi_po_taxidu[m]+"\n")
e.close()