n = int(input())
totalsum = n * (n+1) / 2
sum1 = totalsum / 2
sum2 = totalsum / 2
group1 = []
group2 = []

for i in range(n, 0, -1):
    if i <= sum1:
        group1.append(i)
        sum1 -= i
    else:
        group2.append(i)
        sum2 -= i

if sum1 == 0 and sum2 == 0:
    print("YES")
    print(len(group1))
    for n in group1:
        print(n, end=" ")
    print()
    print(len(group2))
    for n in group2:
        print(n, end=" ")
else:
    print("NO")