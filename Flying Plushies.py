fly = int(input())
plushies = int(input())
count = 0

for i in range(plushies):
    height = int(input())
    if height >= fly:
        count += 1

print(count)