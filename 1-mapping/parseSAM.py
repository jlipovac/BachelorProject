f = open("alignment.sam", 'r')
lines = f.readlines()
dictionary = {}
for line in lines:
    if line[0]=="@":
        continue
    else:
        l = line.split("\t")
        if l[2]=='*':
            continue
        else:
            if l[0] in dictionary:
                (dictionary[l[0]])[0] += 1
                (dictionary[l[0]])[1] += int(l[4])
                (dictionary[l[0]])[2].append(l[3])
            else:
                dictionary[l[0]] = [1, int(l[4]), [l[3]]]
f.close()
out = open("output.txt", 'w')
for x in dictionary:
    out.write(x + "\t" + str(dictionary[x][0]) + "\t" + ", ".join(dictionary[x][2]) + "\t" + str(dictionary[x][1]/dictionary[x][0]) + "\n")
out.close()