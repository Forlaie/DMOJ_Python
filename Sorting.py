times = int(input())
num = []

for i in range(times):
    n = int(input())
    num.append(n)

num.sort()

for i in range(len(num)):
    print(num[i])