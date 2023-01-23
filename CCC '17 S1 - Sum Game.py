times = int(input())
swift = input()
sema = input()
sum1 = 0
sum2 = 0
day = 0

swift = swift.split()
swift = map(int, swift)
swift = list(swift)

sema = sema.split()
sema = map(int, sema)
sema = list(sema)

for i in range(times):
    sum1 += swift[i]
    sum2 += sema[i]
    if sum1 == sum2:
        day = i+1

print(day)