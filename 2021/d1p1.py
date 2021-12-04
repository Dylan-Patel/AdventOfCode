content = open("input.txt", "r")
input = [int(i) for i in content.read().split("\n")]

counter = 0
for a in range((len(input) - 1)):
      if input[a+1] > input [a]:
      	counter += 1

print(counter)