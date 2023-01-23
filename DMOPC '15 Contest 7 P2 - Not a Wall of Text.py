text = input()
count = 1
for i in range(len(text)):
    if text[i] == " ":
        count += 1
print(count)