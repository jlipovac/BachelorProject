from Bio import SeqIO

def main():
    sequences = list()
    for record in SeqIO.parse("../chr19_two_mio/reads.fasta", "fasta"):
        id_B_S, E = record.description.split("end=")
        record.description = id_B_S + "length=" + str(len(record.seq))
        sequences.append(record)

    with open("assignment_1.fasta", "w") as output_handle:
        SeqIO.write(sequences, output_handle, "fasta")

if __name__ == "__main__":
    main()
