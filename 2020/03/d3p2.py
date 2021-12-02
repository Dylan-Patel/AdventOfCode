content = open("input3.txt", "r")
inputFile = content.read()
inputList = inputFile.split("\n")

# Duplicates each item in list until the length of item is 3x the length of the list (columns = 3 * rows).
while len(inputList[0]) < (7 * len(inputList)):
    for index, row in enumerate(inputList):
        inputList[index] = inputList[index] + inputList[index]

treeCount1 = 0
treeCount2 = 0
treeCount3 = 0
treeCount4 = 0
treeCount5 = 0

for i, row in enumerate(inputList):
    first = inputList[i][i]
    second = inputList[i][i * 3]
    third = inputList[i][i * 5]
    fourth = inputList[i][i * 7]
    if (i * 2) < (len(inputList)):
        fifth = inputList[i * 2][i]
    if (i == (len(inputList) - 1)):
        # print('true')
        j = i / 2
        fifth = inputList[i][j]

    if (first) == '#':
        treeCount1 += 1
        
    if (second) == '#':
        treeCount2 += 1
    
    if (third) == '#':
        treeCount3 += 1
        
    if (fourth) == '#':
        treeCount4 += 1

    if (fifth) == '#':
        treeCount5 += 1

print(treeCount1 * treeCount2 * treeCount3 * treeCount4 * treeCount5)
