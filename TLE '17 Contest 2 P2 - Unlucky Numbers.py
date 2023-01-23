unluckies = int(input())
badnumbers = input()
bad = badnumbers.split(" ")
test = map(int, bad)
test = list(test)

boollist = []
psa = []

for i in range(1000000):
    if i+1 not in test:
        boollist.append(1)
    else:
        boollist.append(0)

for i in range(1000000):
    psa.append(boollist[i])

for i in range(1, len(boollist)):
    psa[i] += psa[i-1]

apartments = int(input())

for i in range(apartments):
    build = int(input())
    print(psa[build-1])
