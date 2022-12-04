from Bio import SeqIO

dictionaryFastq = {}
dictionaryKraken = {}

for read in SeqIO.parse("small_metagenomic_dataset2.fastq", "fastq"):
    desc = str(read.description).split(" ")
    desc = desc[1].split(",")
    desc = desc[0].split("_", 1)
    name = desc[1].replace("_", " ")
    taxid = desc[0]
    dictionaryFastq[read.id] = taxid
    #dictionaryFastq[read.id] = name



file = open("sequences2.kraken", "r")
unclassified = open("unclassified.txt", "w")
for line in file:
    desc = line.split("\t")
    readId = desc[1]
    if desc[0] == "U":
        unclassified.write(readId + "\n")
    else:
        info = desc[2]
        name = info.split("(")
        taxid = name[1]
        taxid = taxid.replace(")", "").split(" ")
        taxid = taxid[1]
        name = name[0]
        name = str(name).strip()
        dictionaryKraken[readId] = taxid
        #dictionaryKraken[readId] = name


correct = open("correct.txt", "w")
correctCounter = 0
wrong = open("wrong.txt", "w")
for i in dictionaryKraken:
    if dictionaryKraken[i] == dictionaryFastq[i]:
        correctCounter += 1
    else:
        wrong.write(i + "\n")

correct.write("Number of correctly classified reads is: " + str(correctCounter))