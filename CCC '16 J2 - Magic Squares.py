first = input()
second = input()
third = input()
fourth = input()

frow = first.split()
frow = map(int, frow)
frow = list(frow)

srow = second.split()
srow = map(int, srow)
srow = list(srow)

trow = third.split()
trow = map(int, trow)
trow = list(trow)

lrow = fourth.split()
lrow = map(int, lrow)
lrow = list(lrow)

if (frow[0] + frow[1] + frow[2] + frow[3]) == (srow[0] + srow[1] + srow[2] + srow[3]) == (trow[0] + trow[1] + trow[2] + trow[3]) == (lrow[0] + lrow[1] + lrow[2] + lrow[3]):
    if (frow[0] + srow[0] + trow[0] + lrow[0]) == (frow[1] + srow[1] + trow[1] + lrow[1]) == (frow[2] + srow[2] + trow[2] + lrow[2]) == (frow[3] + srow[3] + trow[3] + lrow[3]):
        print("magic")
    else:
        print("not magic")
else:
    print("not magic")