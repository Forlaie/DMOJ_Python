# number = int(input())
# if number == 1:
#     print("1")
# elif number =j

# 1 = 1
# 2 = 2
# 3 = 2
# 4 = 3
# 5 = 3
# 6 = 3
# 7 = 2
# 8 = 2
# 9 = 1
# 10 = 1

# find numbers, make sure they are under 5, count

number = int(input())
find = 0
count = 0
total = []

for i in range(number):
    if number - find <= 5 and find <= 5:
        if find not in total:
            count += 1
            total.append(find)
            total.append(number-find)
    find += 1
print(count)
#print(total)