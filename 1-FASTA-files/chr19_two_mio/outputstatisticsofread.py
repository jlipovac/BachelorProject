from Bio import SeqIO
average = []
def Average(polje):
    return sum(polje)/len(polje)
for record in SeqIO.parse("A.fasta", "fasta"):
    l = record.description.split(", ")
    pocetak = (l[1].split('='))[1]
    kraj = (l[2].split('='))[1]
    average.append(int(kraj)-int(pocetak))
print("The shortest read in the file is ->", min(average))
print("There is", len(average), "reads contained in the file!")
print("The average length is ->", round(Average(average), 2))