# Reading input file and creating a list "input":
content = open("input.txt", "r")
input_file = content.read()
input = input_file.split("\n")
#print(input)


# Add up various quantities in input:
length = len(input)
for i in range(length):
    for j in range(length):
        a = input[i]
        b = input[j]
        z = int(a) + int(b)
        if z == 2020:
            break
    else:
        continue
    break

answer = int(a)*int(b)

# Two values which sum to 2020:    
print(str(a) + ', ' + str(b))

print('answer = ' + str(answer))
