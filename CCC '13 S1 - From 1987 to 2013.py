year = int(input())

while True:
    year = int(year)
    year += 1
    year = str(year)
    num = []
    for i in range(len(year)):
        num.append(year[i])
    test = set(num)
    if len(num) == len(test):
        print(year)
        break