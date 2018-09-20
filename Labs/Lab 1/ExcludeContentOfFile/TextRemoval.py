wordsSet = set()
with open('file2.txt') as afile:
    for word in afile.read().split():
            word = word.lower()
            wordsSet.add(word)
newFile = open("new_file.txt", "w")
with open('file1.txt', 'r') as bfile:
    for line in bfile.readlines():
        for word in line.split():
            word = word.lower()
            if word not in wordsSet:
                newFile.write(word)
                newFile.write(' ')
newFile.close()