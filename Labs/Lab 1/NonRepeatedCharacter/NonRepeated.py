userInput = input("Please provide a string:")
count = {}
userInput = userInput.lower()

# assigning count of each character
for c in userInput:
    if(c != ' '):
        count[c] = count.get(c,0) + 1

# return the character that has a count of 1
for k,v in count.items():
    if v == 1:
        print(k)
        break

