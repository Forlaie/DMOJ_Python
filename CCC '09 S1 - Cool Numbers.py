import math

lowest = int(input())
highest = int(input())
num = math.floor(math.pow(lowest, 1/6))
sum = 1
count = 0

while True:
    sum = math.pow(num, 6)
    if sum <= highest and lowest <= sum:
        num += 1
        count += 1
    elif sum > highest:
        break
    elif sum < lowest:
        num += 1

print(count)