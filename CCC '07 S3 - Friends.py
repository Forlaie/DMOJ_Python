students = int(input())
friends = {} #assigned, normal
for i in range(students):
    thing = input()
    assigned, normal = thing.split()
    friends[assigned] = normal

while True:
    find = input()
    if find == "0 0":
        break
    start, end = find.split()
    temp = friends[start]
    count = 0
    answer = False
    if temp == end:
        print(f"Yes {count}")
    else:
        while not answer:
            if temp in friends:
                if friends[temp] != end and temp != start:
                    count += 1
                    temp = friends[temp]
                elif friends[temp] == end:
                    answer = True
                else:
                    break
            else:
                break
        if not answer:
            print("No")
        else:
            print(f"Yes {count+1}")