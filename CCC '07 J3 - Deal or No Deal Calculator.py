opened = int(input())
money = {1: 100, 2: 500, 3: 1000, 4: 5000, 5: 10000, 6: 25000, 7: 50000, 8: 100000, 9: 500000, 10: 1000000}

for i in range(opened):
    case = int(input())
    money.pop(case)

banker = int(input())

average = sum(money.values())
average = average/(10-opened)

if banker > average:
    print("deal")
else:
    print("no deal")