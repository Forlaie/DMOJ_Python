rabbits = int(input())
groups = int(input())

if rabbits % groups == 0:
    print(0)
elif rabbits < groups:
    print(groups-rabbits)
else:
    remainder = rabbits % groups
    other = (groups * (int(rabbits/groups)+1)) - rabbits
    if remainder <= other:
        print(remainder)
    else:
        print(other)