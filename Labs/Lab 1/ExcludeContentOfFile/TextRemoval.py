wordsSet = set()
with open('file2.txt') as afile:
    for word in afile.read().split():
            # converting text to lower case
            word = word.lower()
            #adding contents of file 2 to wordSet
            wordsSet.add(word)
newFile = open("new_file.txt", "w")
with open('file1.txt', 'r') as bfile:
    for line in bfile.readlines():
        for word in line.split():
            word = word.lower()
            # check and add only if the word is not in file1
            if word not in wordsSet:
                newFile.write(word)
                newFile.write(' ')
newFile.close()