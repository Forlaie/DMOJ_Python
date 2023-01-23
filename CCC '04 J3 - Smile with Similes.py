numA = int(input())
numN = int(input())

adjectives = []
for i in range(numA):
    word = input()
    adjectives.append(word)

nouns = []
for i in range(numN):
    word2 = input()
    nouns.append(word2)

for i in range(numA):
    for j in range(numN):
        print(adjectives[i], "as", nouns[j])