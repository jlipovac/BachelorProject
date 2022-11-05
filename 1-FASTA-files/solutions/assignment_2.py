from Bio import SeqIO

def main():
    len_reference = 0
    for record in SeqIO.parse("../chr19_two_mio/reference.fasta", "fasta"):
        print("Length of the reference sequence: " + str(len(record.seq)))
        len_reference = len(record.seq)

    len_combined = 0
    for record in SeqIO.parse("../chr19_two_mio/reads.fasta", "fasta"):
        len_combined += len(record.seq)
    print("Length of the combined sequence of the reads: " + str(len_combined))

    print("Coverage of the given dataset: " + str(len_combined/len_reference))

if __name__ == "__main__":
    main()
