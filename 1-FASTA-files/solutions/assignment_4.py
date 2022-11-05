from Bio import SeqIO

def main():
    len_reference = 0
    for record in SeqIO.parse("../chr19_two_mio/reference.fasta", "fasta"):
        len_reference = len(record.seq)
    shortest = len_reference
    avg_length = 0
    num_sequences = 0
    for record in SeqIO.parse("A.fasta", "fasta"):
        if len(record.seq) < shortest:
            shortest = len(record.seq)
        num_sequences += 1
        avg_length += len(record.seq)

    avg_length /= num_sequences
    print("The shortest read in the file is " + str(shortest) + " bases long.")
    print("There are " + str(num_sequences) + " reads in the file.")
    print("The average length of a read is " + str(avg_length) + " bases.")

if __name__ == "__main__":
    main()
