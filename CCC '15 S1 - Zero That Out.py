times = int(input())
numbers = []
for i in range(times):
    num = int(input())
    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)

sumNum = 0
for i in range(len(numbers)):
    sumNum += numbers[i]
print(sumNum)