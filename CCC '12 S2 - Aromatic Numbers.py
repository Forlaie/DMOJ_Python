baseToNum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

aromatic = input()
result = 0

if len(aromatic) > 2:
    for i in range(0, len(aromatic)-2, 2):
        num = int(aromatic[i])
        base = baseToNum[aromatic[i+1]]
        nextBase = baseToNum[aromatic[i+3]]
        if nextBase > base:
            result -= num*base
        else:
            result += num*base
num = int(aromatic[-2])
base = baseToNum[aromatic[-1]]
result += num*base
print(result)