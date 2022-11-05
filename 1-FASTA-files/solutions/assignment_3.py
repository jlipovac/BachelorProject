from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def main():
    len_reference = 0
    for record in SeqIO.parse("../chr19_two_mio/reference.fasta", "fasta"):
        len_reference = len(record.seq)

    A_from, A_to, B_from, B_to = 500000, 600000, 1500000, 1600000
    A_records, B_records = list(), list()
    A_index, B_index = 1, 1
    len_A, len_B = 0, 0
    for record in SeqIO.parse("../chr19_two_mio/reads.fasta", "fasta"):
        id, start = record.description.split("start=")[0].split(" ")[0], record.description.split("start=")[1].split(", end=")[0]
        if (int(start) >= A_from and int(start) <= A_to):
            description_no_id = "strand=" + record.description.split("strand=")[1]
            new_description = str(A_index) + " " + description_no_id
            new_record = SeqRecord(record.seq, str(A_index), record.name, new_description, record.dbxrefs, record.features, record.annotations, record.letter_annotations)
            A_records.append(new_record)
            A_index += 1
            len_A += len(record.seq)
        elif (int(start) >= B_from and int(start) <= B_to):
            description_no_id = "strand=" + record.description.split("strand=")[1]
            new_description = str(B_index) + " " + description_no_id
            new_record = SeqRecord(record.seq, str(B_index), record.name, new_description, record.dbxrefs, record.features, record.annotations, record.letter_annotations)
            B_records.append(new_record)
            B_index += 1
            len_B += len(record.seq)

    print("Coverage of read set \"A\": " + str(len_A / len_reference))
    print("Coverage of read set \"B\": " + str(len_B / len_reference))

    with open("A.fasta", "w") as output_handle:
        SeqIO.write(A_records, output_handle, "fasta")

    with open("B.fasta", "w") as output_handle:
        SeqIO.write(B_records, output_handle, "fasta")


if __name__ == "__main__":
    main()
