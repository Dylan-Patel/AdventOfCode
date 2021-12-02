content = open("input.txt", "r")
input = [int(i) for i in content.read().split("\n")]

counter = 0
prevSum = sum(input[0:2])

for i in range(2, len(input)):
    newSum = prevSum + input[i] - input[i-3] 
    if newSum > prevSum:
        counter += 1
print("Total number of increases:", counter)