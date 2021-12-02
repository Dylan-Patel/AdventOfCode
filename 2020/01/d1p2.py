# Reading input file and creating a list "input":
content = open("input.txt", "r")
input_file = content.read()
input = input_file.split("\n")
#print(input)


# Add up various quantities in input:
length = len(input)
for i in range(length):
    for j in range(length):
        for k in range(length):
            a = input[i]
            b = input[j]
            c = input[k]
            z = int(a) + int(b) + int(c)
            if z == 2020:
                break
        else:
            continue
        break
    else:
        continue
    break

answer = int(a)*int(b)*int(c)

# Two values which sum to 2020:    
print(str(a) + ', ' + str(b) + ', ' + str(c))

print('answer = ' + str(answer))
