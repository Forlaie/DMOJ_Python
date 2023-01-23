quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

count = 0

while quarters > 0:
    first += 1
    quarters -= 1
    count += 1
    if first == 35:
        quarters += 30
        first = 0
    if quarters <= 0:
        break

    second += 1
    quarters -= 1
    count += 1
    if second == 100:
        quarters += 60
        second = 0
    if quarters <= 0:
        break

    third += 1
    quarters -= 1
    count += 1
    if third == 10:
        quarters += 9
        third = 0
    if quarters <= 0:
        break

print("Martha plays", count, "times before going broke.")