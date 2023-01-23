daytime = float(input())
evening = float(input())
weekend = float(input())

if daytime >= 100:
    ad = daytime-100
else:
    ad = 0

if daytime >= 250:
    bd = daytime-250
else:
    bd = 0

a_dcost = ad*0.25
a_ecost = evening*0.15
a_wcost = weekend*0.2

b_dcost = bd*0.45
b_ecost = evening*0.35
b_wcost = weekend*0.25

a = a_dcost + a_ecost + a_wcost
b = b_dcost + b_ecost + b_wcost

a = round(a, 2)
b = round(b, 2)

print("Plan A costs", a)
print("Plan B costs", b)

if a < b:
    print("Plan A is cheapest.")
elif b < a:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")