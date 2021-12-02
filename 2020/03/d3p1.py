content = open("input3.txt", "r")
inputFile = content.read()
inputList = inputFile.split("\n")

# Duplicates each item in list until the length of item is 3x the length of the list (columns = 3 * rows).
while len(inputList[0]) < (3 * len(inputList)):
    for index, row in enumerate(inputList):
        inputList[index] = inputList[index] + inputList[index]

treeCount = 0

for i, row in enumerate(inputList):
    if (inputList[i][i * 3]) == '#':
        treeCount += 1

print(treeCount)

