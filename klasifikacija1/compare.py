from Bio import SeqIO
import os

dictionaryFastqTax = {}
dictionaryKrakenTax = {}
dictionaryFastqName = {}
dictionaryKrakenName = {}

for read in SeqIO.parse("small_metagenomic_dataset2.fastq", "fastq"):
    desc = str(read.description).split(" ")
    desc = desc[1].split(",")
    desc = desc[0].split("_", 1)
    name = desc[1].replace("_", " ")
    taxid = desc[0]
    dictionaryFastqTax[read.id] = taxid
    dictionaryFastqName[read.id] = name



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
        dictionaryKrakenTax[readId] = taxid
        dictionaryKrakenName[readId] = name


correctName = open("correctByName.txt", "w")
correctTaxId = open("correctByTaxId.txt", "w")
correctCounterName = 0
correctCounterTaxId = 0
wrongName = open("wrongByName.txt", "w")
wrongTaxId = open("wrongByTaxId.txt", "w")
correct = open("correct.txt", "w")
for i in dictionaryKrakenTax:
    if dictionaryKrakenTax[i] == dictionaryFastqTax[i]:
        correctCounterTaxId += 1
        correct.write(i + "\n")
    else:
        wrongTaxId.write(i + "\n")

for i in dictionaryKrakenName:
    if dictionaryKrakenName[i] == dictionaryFastqName[i]:
        correctCounterName += 1
        correct.write(i + "\n")
    else:
        wrongName.write(i + "\n")

correctTaxId.write("Number of correctly classified reads by TaxId is: " + str(correctCounterTaxId) + "\n")
correct.close()
correctTaxId.close()
correctTaxId = open("correctByTaxId.txt", 'a+')
correct = open("correct.txt", 'r')
correctTaxId.write(correct.read())
correct.close()
correctTaxId.close()

correctName.write("Number of correctly classified reads by name is: " + str(correctCounterName) + "\n")
correct.close()
correctName.close()
correctName = open("correctByName.txt", 'a+')
correct = open("correct.txt", 'r')
correctName.write(correct.read())
correct.close()
correctName.close()

os.remove("correct.txt")