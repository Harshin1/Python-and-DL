import csv

codonSequence = "AAAGGGTTTTTT"
print("The codon sequence is: " + codonSequence)
sequenceList = [codonSequence[i:i+3] for i in range(0, len(codonSequence), 3)]
print("The individual codons are ", end="")
print(sequenceList)
d = {};

for val in sequenceList:
    with open("codon.txt") as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            if row[0] == val:
                if row[1] in d:
                    d[row[1]] = d.get(row[1]) + 1;
                else:
                    d[row[1]] = 1;

print(d)



