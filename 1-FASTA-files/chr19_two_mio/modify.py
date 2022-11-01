from Bio import SeqIO

filename = 'reads.fasta'
sequences = []

for record in SeqIO.parse(filename, 'fasta'):
    desc = record.description
    desc_statrt = desc.split("end")
    new_desc = desc_statrt[0] + " length=" + str(len(record))
    record.description = new_desc
    sequences.append(record)

SeqIO.write(sequences, "modify.fasta", "fasta")

