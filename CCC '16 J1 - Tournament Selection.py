wincount = 0

for i in range (6):
    round = input()
    if round == "W":
        wincount += 1
if wincount >= 5:
    print("1")
elif wincount >= 3:
    print("2")
elif wincount >= 1:
    print("3")
else:
    print("-1")