scount = 0
tcount = 0

times = int(input())

for i in range(times):
    sentence = input()
    words = list(sentence)
    for i in words:
        if i == "s" or i == "S":
            scount += 1
        if i == "t" or i == "T":
            tcount += 1

if tcount > scount:
    print("English")
else:
    print("French")