num = int(input())
count = {}
for i in range(num):
    reading = int(input())
    if reading not in count:
        count[reading] = 1
    else:
        count[reading] += 1

sorted_values = sorted(count.values(), reverse=True)
maxCount = sorted_values[0]
secondMaxCount = sorted_values[0]
for value in sorted_values:
    if value != maxCount:
        secondMaxCount = value
        break

maxNums = []
secondMaxNums = []

for key in count:
    if count[key] == maxCount:
        maxNums.append(key)
    if count[key] == secondMaxCount:
        secondMaxNums.append(key)

if len(maxNums) > 1:
    maxNums.sort()
    print(abs(maxNums[0] - maxNums[-1]))
else:
    secondMaxNums.sort()
    print(max(abs(maxNums[0] - secondMaxNums[0]), abs(maxNums[0] - secondMaxNums[-1])))
