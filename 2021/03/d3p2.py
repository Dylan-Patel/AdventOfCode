from collections import Counter
input = open('input.txt', 'r').read().splitlines()

rowL = len(input[0])
oxyGen = input.copy()
for i in range(rowL):
    N = len(oxyGen)
    if N == 1: break
    count = len([j for j in oxyGen if j[i] == '1'])
    if count >= N / 2:
        oxyGen = [j for j in oxyGen if j[i] == '1']
    else:
        oxyGen = [j for j in oxyGen if j[i] == '0']
oxyGen = int(oxyGen[0], 2)

co2Scrub = input.copy()
for i in range(rowL):
    N = len(co2Scrub)
    if N == 1: break
    count = len([j for j in co2Scrub if j[i] == '1'])
    if count >= N / 2:
        co2Scrub = [j for j in co2Scrub if j[i] == '0']
    else:
        co2Scrub = [j for j in co2Scrub if j[i] == '1']
co2Scrub = int(co2Scrub[0], 2)

lifeSupport = oxyGen * co2Scrub
print('Life support rating:', lifeSupport)