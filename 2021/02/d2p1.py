content = open("input.txt", "r")
input = content.read().split("\n")
i,h,d = [0,0,0]

while i < len(input):
	quant = int(input[i][-1])
	if 'forward' in input[i]:
		h += quant
	if 'up' in input[i]:
		d -= quant
	if 'down' in input[i]:
		d += quant
	i += 1
	
print(h,d)