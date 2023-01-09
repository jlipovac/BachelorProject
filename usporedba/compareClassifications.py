dictionaryTaxIdContigLenth = {}
dictionaryTaxIdContigPercentage = {}
dictionaryTaxIdReadPercentage = {}

file = open("kraken2.out", "r")
compareTaxid = open("compareTaxid.txt", "w")
contigCounter = 0
for line in file:
    contigCounter += 1
    desc = line.split("\t")
    contigNum = desc[1]
    if desc[0] == "C":
        length = int(desc[3])
        info = desc[2]
        taxid = info.split("taxid ")
        taxid = taxid[1].replace(")", "")
        if taxid in dictionaryTaxIdContigLenth:
            dictionaryTaxIdContigLenth[taxid] = dictionaryTaxIdContigLenth[taxid] + length
            dictionaryTaxIdContigPercentage[taxid] = dictionaryTaxIdContigPercentage[taxid] + 1
        else:
            dictionaryTaxIdContigLenth[taxid] = length
            dictionaryTaxIdContigPercentage[taxid] = 1
            dictionaryTaxIdReadPercentage[taxid] = 0


file.close()


file = open("sequences2.kraken", "r")
readCounter = 0
for line in file:
    readCounter += 1
    desc = line.split("\t")
    if desc[0] == "C":
        info = desc[2]
        taxid = info.split("taxid ")
        taxid = taxid[1].replace(")", "")
        if taxid in dictionaryTaxIdReadPercentage:
            dictionaryTaxIdReadPercentage[taxid] = dictionaryTaxIdReadPercentage[taxid] + 1

        

compareTaxid.write("taxid\tread%\tcontig%\tcontig length\n")
sumR = 0
sumC = 0
for key in dictionaryTaxIdReadPercentage:
    percentageRead = str(round((dictionaryTaxIdReadPercentage[key] / readCounter * 100),4))
    percentageContig = str(round((dictionaryTaxIdContigPercentage[key] / contigCounter * 100),4))
    sumR += float(percentageRead)
    sumC += float(percentageContig)
    compareTaxid.write(str(key) + "\t" + percentageRead + "%\t" + percentageContig + "%\t" + str(dictionaryTaxIdContigLenth[key]) + "\n")


compareTaxid.write("\nIn total: " + str(round(sumR, 2)) + "% of reads and " + str(round(sumC, 2)) + "% of contigs.")


file.close()
compareTaxid.close()