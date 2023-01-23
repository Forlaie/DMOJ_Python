times = int(input())
for i in range(times):
    num = int(input())
    sum = 0
    for j in range(1, num//+1):
        if num%j == 0:
            sum += j
    if sum < num:
        print(f"{num} is a deficient number.")
    elif sum > num:
        print(f"{num} is an abundant number.")
    else:
        print(f"{num} is a perfect number.")