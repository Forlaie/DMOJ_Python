number = int(input())
count = 0

if number == 1 or number == 2 or number == 3:
    print(count)
else:
    times = number - 3
    number -= 2
    for i in range(times):
        number -= 1
        for j in range(1,number+1):
            count += j
    print(count)