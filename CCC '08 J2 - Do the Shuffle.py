playlist = ["A", "B", "C", "D", "E"]
change = playlist.copy()
go = "yes"

while go == "yes":
    button = int(input())
    times = int(input())

    if button == 1:
        for i in range(times):
            change.append(playlist[0])
            change.pop(0)
            playlist = change.copy()

    elif button == 2:
        for i in range(times):
            change.insert(0, playlist[-1])
            change.pop(-1)
            playlist = change.copy()

    elif button == 3:
        for i in range(times):
            change[0] = playlist[1]
            change[1] = playlist[0]
            playlist = change.copy()

    else:
        go = "no"

for i in change:
    print(i, end=" ")