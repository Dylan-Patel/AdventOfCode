import re

# Reading input file and creating a list "input"
content = open("input.txt", "r")
input_file = content.read()
input = input_file.split("\n")

i = 0
for x in range(len(input)):
    colonized = (re.sub("[-]", ":", input[x]))
    input_split = colonized.split(":")
    
    pos1 = input_split[0]
    policyChar = input_split[1][-1]
    password = input_split[2][1:]

    e = input_split[1]
    pos2 = e[0:-2]
    
    a = int(pos1) - 1
    b = int(pos2) - 1
    if (policyChar == password[a]):
        if (policyChar != password[b]):
            # print('true')
            i += 1
    if (policyChar != password[a]):
        if (policyChar == password[b]):
            # print('true')
            i += 1

print(i)
