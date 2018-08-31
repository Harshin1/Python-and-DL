s = input('Enter a list of numbers: ')
numbers = list(map(int, s.split()))
tupleNum = (numbers[0],numbers[-1])
print(tupleNum)