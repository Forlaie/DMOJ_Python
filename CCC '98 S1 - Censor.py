lines = int(input())
for i in range(lines):
    text = input()
    splitText = text.split()
    censored = ""
    for j in range(len(splitText)):
        if len(splitText[j]) == 4:
            censored += "****"
        else:
            censored += splitText[j]
        censored += " "
    print(censored.strip())