

file = open("kraken2.out", "r")
unclassified = open("unclassifiedContigs.txt", "w")
classified = open("classifiedContigs.txt", "w")
for line in file:
    desc = line.split("\t")
    contigNum = desc[1]
    if desc[0] == "U":
        unclassified.write(contigNum + "\n")
    else:
        info = desc[2]
        name = info.split("(")
        taxid = name[1]
        taxid = taxid.replace(")", "")
        classified.write(contigNum + "\t" + taxid + "\n")

file.close()
unclassified.close()
classified.close()
