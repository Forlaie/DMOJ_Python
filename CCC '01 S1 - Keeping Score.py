cards = input()

clubIndex = cards.index("C")
diamondIndex = cards.index("D")
heartIndex = cards.index("H")
spadeIndex = cards.index("S")

clubs = cards[clubIndex+1: diamondIndex]
diamonds = cards[diamondIndex+1: heartIndex]
hearts = cards[heartIndex+1: spadeIndex]
spades = cards[spadeIndex+1:]

clubPoints = 0
diamondPoints = 0
heartPoints = 0
spadePoints = 0

clubPoints += clubs.count("A")*4 + clubs.count("K")*3 + clubs.count("Q")*2 + clubs.count("J")*1
diamondPoints += diamonds.count("A")*4 + diamonds.count("K")*3 + diamonds.count("Q")*2 + diamonds.count("J")*1
heartPoints += hearts.count("A")*4 + hearts.count("K")*3 + hearts.count("Q")*2 + hearts.count("J")*1
spadePoints += spades.count("A")*4 + spades.count("K")*3 + spades.count("Q")*2 + spades.count("J")*1

if len(clubs) == 0:
    clubPoints += 3
elif len(clubs) == 1:
    clubPoints += 2
elif len(clubs) == 2:
    clubPoints += 1

if len(diamonds) == 0:
    diamondPoints += 3
elif len(diamonds) == 1:
    diamondPoints += 2
elif len(diamonds) == 2:
    diamondPoints += 1

if len(hearts) == 0:
    heartPoints += 3
elif len(hearts) == 1:
    heartPoints += 2
elif len(hearts) == 2:
    heartPoints += 1

if len(spades) == 0:
    spadePoints += 3
elif len(spades) == 1:
    spadePoints += 2
elif len(spades) == 2:
    spadePoints += 1

clubCards = ""
for i in range(len(clubs)):
    clubCards += clubs[i] + " "
diamondCards = ""
for i in range(len(diamonds)):
    diamondCards += diamonds[i] + " "
heartCards = ""
for i in range(len(hearts)):
    heartCards += hearts[i] + " "
spadeCards = ""
for i in range(len(spades)):
    spadeCards += spades[i] + " "

print("Cards Dealt Points")
print("Clubs " + clubCards + str(clubPoints))
print("Diamonds " + diamondCards + str(diamondPoints))
print("Hearts " + heartCards + str(heartPoints))
print("Spades " + spadeCards + str(spadePoints))
print(" Total " + str(clubPoints+diamondPoints+heartPoints+spadePoints))