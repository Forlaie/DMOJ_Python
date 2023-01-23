word = input()
canada = ""

while word != "quit!":
    if len(word) > 4:
        if word[-1] == "r" and word[-2] == "o" and word[-3] not in "aeiou":
            for i in range (len(word)-1):
                canada += word[i]
            canada += "ur"
            print(canada)
            canada = ""
        else:
            print(word)
    else:
        print(word)
    word = input()