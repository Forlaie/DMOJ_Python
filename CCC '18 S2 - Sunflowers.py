lines = int(input())
test = []
a = 0
b = 0
# test = [[] for i in range(lines)]
# print(test)
for i in range(lines):
    check = input()
    test.append(check.split())

for i in range(lines):
    for j in range(len(test[i])):
        test[i][j] = int(test[i][j])

if test[0][0] < test[0][-1] and test[0][0] < test[-1][-1] and test[0][0] < test[-1][0]:
    for i in range(lines):
        thing = ""
        for j in range(len(test[i])):
            thing += str(test[i][j])
            if test[i][j] != test[i][-1]:
                thing += " "
            else:
                print(thing)
                thing = ""
elif test[0][-1] < test[0][0] and test [0][-1] < test[-1][-1] and test[0][-1] < test[-1][0]:
    a = 0
    b = -1
    for i in range(lines):
        thing = ""
        a = 0
        for j in range(len(test[i])):
            thing += str(test[a][b])
            if test[a] != test[-1]:
                thing += " "
            else:
                print(thing)
                thing = ""
                b -= 1
            a += 1
elif test[-1][-1] < test[0][0] and test[-1][-1] < test[0][-1] and test[-1][-1] < test[-1][0]:
    a = 0
    b = -1
    for i in range(lines):
        thing = ""
        a -= 1
        b = -1
        for j in range(len(test[i])):
            thing += str(test[a][b])
            if test[a][b] != test[a][0]:
                thing += " "
                b -= 1
            else:
                print(thing)
                thing = ""
                b -= 1
else:
    a = 0
    b = -1
    for i in range(lines):
        thing = ""
        a = -1
        b += 1
        for j in range(len(test[i])):
            thing += str(test[a][b])
            if test[a] != test[0]:
                thing += " "
                a -= 1
            else:
                print(thing)
                thing = ""
                a = -1