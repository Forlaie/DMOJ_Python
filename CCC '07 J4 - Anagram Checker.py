phrase1 = input()
phrase2 = input()
letters1 = list(phrase1)
letters2 = list(phrase2)
isAnagram = True

while letters1.count(' ') > 0:
    letters1.remove(' ')

while letters2.count(' ') > 0:
    letters2.remove(' ')

if len(letters1) != len(letters2):
    print("Is not an anagram.")
    isAnagram = False
else:
    for char in letters1:
        try:
            letters2.remove(char)
        except:
            print("Is not an anagram.")
            isAnagram = False
if isAnagram:
    print("Is an anagram.")
