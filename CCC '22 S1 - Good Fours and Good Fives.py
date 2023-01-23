num = int(input())
count = 0

for i in range(num//5+1):
    if (num - 5*i) % 4 == 0:
        count += 1
print(count)
