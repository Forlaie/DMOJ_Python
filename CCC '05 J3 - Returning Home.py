location = ""
list = []
a = -2
while location != "SCHOOL":
    direction = input()
    location = input()
    list.append(direction)
    list.append(location)

for i in range(int(len(list)/2)):
    sentence = "Turn "
    if list[a] == "R":
        sentence += "LEFT "
    else:
        sentence += "RIGHT "
    if abs(a) != len(list):
        sentence += "onto "
        sentence += list[a-1]
        sentence += " street."
    else:
        sentence += "into your HOME."
    print(sentence)
    a -= 2