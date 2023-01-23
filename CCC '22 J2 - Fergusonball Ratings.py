numOfPlayers = int(input())
goodStars = 0
allGoodStars = True
for i in range(numOfPlayers):
    scores = int(input())
    fouls = int(input())
    stars = scores*5 - fouls*3
    if stars > 40:
        goodStars += 1
    else:
        allGoodStars = False

if allGoodStars:
    print(str(goodStars) + "+")
else:
    print(goodStars)