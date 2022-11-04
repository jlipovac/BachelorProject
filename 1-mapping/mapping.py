from simplesam import Reader

file = open('alignment.sam', 'r')
in_sam = Reader(file)

dictionary = {}
for read in in_sam:
    if(read.mapped):
        read_id = str(read.qname)
        parts = str(read).split("\t")
        if parts[0] in dictionary:
            (dictionary[read_id])[0] += 1
            (dictionary[read_id])[1] += ", " + parts[3]
            (dictionary[read_id])[2]+= int(parts[4])
        else:
           dictionary[read_id] = [1, str(parts[3]), int(parts[4])]



headers = ["Read ID", "#mappings", "start positions", "Avg quality"]
out = open("output.txt", 'w')
out.write(f'{headers[0]: <40}{headers[1]: <15}{headers[2]: <75}{headers[3]: <15}')
out.write("\n")
for key, value in dictionary.items():
    out.write(f'{key: <40}{value[0]: <15}{value[1]: <75}{" " +str(round(value[2]/value[0], 2)): <15}')
    out.write("\n")
out.close()    