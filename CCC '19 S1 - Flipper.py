ogf = [1, 2]
ogl = [3, 4]
changef = [1, 2]
changel = [3, 4]

flips = input()

for i in range(len(flips)):
    if flips[i] == "H":
        changef = ogl.copy()
        changel = ogf.copy()
        ogf = changef.copy()
        ogl = changel.copy()
    else:
        changef[0] = ogf[1]
        changef[1] = ogf[0]
        changel[0] = ogl[1]
        changel[1] = ogl[0]
        ogf = changef.copy()
        ogl = changel.copy()

print(ogf[0], ogf[1])
print(ogl[0], ogl[1])