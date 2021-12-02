import re

# Reading input file and creating a list "input"
content = open("input.txt", "r")
input_file = content.read()
input = input_file.split("\n")

i = 0
for x in range(len(input)):
    colonized = (re.sub("[-]", ":", input[x]))
    input_split = colonized.split(":")
    
    lowerLimit = input_split[0]
    policyChar = input_split[1][-1]
    password = input_split[2]

    e = input_split[1]
    upperLimit = e[0:-2]
    

    count = password.count(policyChar)
    if (int(lowerLimit) <= count & count <= int(upperLimit)):
        print('true')
        i += 1
    else:
        print('false')

print(i)




"""
0: Create valid password counter

for x in range(len(input)):
    lowerLimit = 

1: Loop for each item in list

2: Create integer for characters 1 and 3 in list item (range limits)

3: Create string for password policy character (ppc)

4: Create string for character 4 onwards in list item (password)

5: Check how many times the ppc appears in the password.

6: Determine if this no. of repeats is within the range limits


7: If true: add 1 to counter



 """
