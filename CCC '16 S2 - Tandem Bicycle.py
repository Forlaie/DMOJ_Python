question = int(input())
people = int(input())
dmoj = input()
wcipeg = input()

dlist = dmoj.split()
wlist = wcipeg.split()
dlist = map(int, dlist)
wlist = map(int, wlist)
dlist = list(dlist)
wlist = list(wlist)

sum = 0

if question == 1:
    dlist.sort(reverse=True)
    wlist.sort(reverse=True)
    for i in range(len(dlist)):
        if dlist[i] >= wlist[i]:
            sum += dlist[i]
        else:
            sum += wlist[i]
    print(sum)
else:
    dlist.sort(reverse=True)
    wlist.sort()
    for i in range(len(dlist)):
        if dlist[i] >= wlist[i]:
            sum += dlist[i]
        else:
            sum += wlist[i]
    print(sum)