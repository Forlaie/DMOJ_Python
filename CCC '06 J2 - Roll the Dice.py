first = int(input())
second = int(input())
count = 0

for i in range(1, first+1):
    if 0 < 10-i <= second:
        count += 1

if count == 1:
    print("There is", count, "way to get the sum 10.")
else:
    print("There are", count, "ways to get the sum 10.")