number = int(input())
times = int(input())
numberlist = []
answer = number
shiftnum = str(number)

for i in range(times):
    shiftnum += "0"
    answer += int(shiftnum)
print(answer)

# print(numberlist)
# testing = numberlist[0] + numberlist[1] + "0"
# print(testing)

# for i in range(len(number)):
#     numberlist.append(number[i])
# for i in range(times)
#     answer += int(shiftnum)
# for i in range(len(number)):
#     shiftnum += numberlist[i]
