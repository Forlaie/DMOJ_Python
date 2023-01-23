low = int(input())
high = int(input())

count = 0
num = 0

for i in range(low, high+1):
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 4:
        num += 1
    count = 0

print("The number of RSA numbers between", low, "and", high, "is", num)