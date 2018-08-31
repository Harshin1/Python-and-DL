f = open("words.txt", "r")
data = f.read()
f.close()
words = data.split(" ")
print(len(words))
characters = 0
for word in words:
    characters += len(word)
print(characters)
