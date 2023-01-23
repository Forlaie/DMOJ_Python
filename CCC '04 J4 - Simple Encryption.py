keyword = input()
message = input()
cleanmessage = ""
for a in message:
    if a.isalpha():
        cleanmessage += a

coded = ""
while len(cleanmessage) != 0:
    if len(cleanmessage) >= len(keyword):
        row = cleanmessage[:len(keyword)]
        cleanmessage = cleanmessage[len(keyword):]
    else:
        row = cleanmessage
        cleanmessage = ""

    for i in range(len(row)):
        newchar = ord(row[i]) + ord(keyword[i])-65
        if newchar > 90:
            newchar -= 26
        coded += chr(newchar)
print(coded)
#BCWXONKFOTKKFZVI