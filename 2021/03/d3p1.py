from collections import Counter
input = open("input.txt", "r").read().splitlines()

rowL = len(input[0])
N = len(input)
gamma,epsilon = [0,0]

for i in range(rowL):
    count = len([j for j in input if j[i] == '1'])
    d = 2**(rowL-i-1)
    if (count > (N - count)):
        gamma += d
    if (count < (N - count)):
        epsilon += d

decimal = gamma * epsilon
print('Power consumption:',decimal)