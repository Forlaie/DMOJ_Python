word = input()
count = 0
word = word.split()

if "False" in word:
    count = len(word)-1
    if count % 2 == 0:
        print("False")
    else:
        print("True")
else:
    count = len(word) - 1
    if count % 2 == 0:
        print("True")
    else:
        print("False")