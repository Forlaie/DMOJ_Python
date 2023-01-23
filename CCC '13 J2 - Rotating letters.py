word = input()
answer = None
for i in range(len(word)):
    if word[i] == "I" or word[i] == "O" or word[i] == "S" or word[i] == "H" or word[i] == "Z" or word[i] == "X" or word[i] == "N":
        answer = True
    else:
        answer = False
        break
if answer:
    print("YES")
else:
    print("NO")