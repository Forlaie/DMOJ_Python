athree = int(input())
atwo = int(input())
aone = int(input())

bthree = int(input())
btwo = int(input())
bone = int(input())

ascore = (athree*3) + (atwo*2) + aone
bscore = (bthree*3) + (btwo*2) + bone

if ascore > bscore:
    print("A")
elif bscore > ascore:
    print("B")
else:
    print("T")