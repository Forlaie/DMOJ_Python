times = int(input())
eligible = "No"
for i in range(times):
    birthday = input()
    year, month, day = birthday.split()
    year = int(year)
    month = int(month)
    day = int(day)
    if year < 1989:
        eligible = "Yes"
    elif year == 1989 and month < 2:
        eligible = "Yes"
    elif year == 1989 and month == 2 and day <= 27:
        eligible = "Yes"
    else:
        eligible = "No"
    print(eligible)