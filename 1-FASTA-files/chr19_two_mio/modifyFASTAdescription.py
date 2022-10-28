from Bio import SeqIO
sequences = []
for record in SeqIO.parse("reads.fasta", "fasta"):
    record.description = record.description.replace("end", "length")
    lista = record.description.split(", ")
    begin = (lista[1].split('='))[1]
    stop = (lista[2].split('='))[1]
    record.description = record.description.replace(stop,str(int(stop)-int(begin)))
    sequences.append(record)
SeqIO.write(sequences, "first.fasta", "fasta")