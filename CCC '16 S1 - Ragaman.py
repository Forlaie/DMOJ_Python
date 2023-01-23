word = input()
anagram = input()
good = True
wordlist = list(word)
anagramlist = list(anagram)
wordlist.sort()
anagramlist.sort()
anagramlist.reverse()

def tisa(word, anagram, wordlist, anagramlist):
    if len(word) != len(anagram):
        return False
    else:
        for i in range(len(anagramlist)):
            if anagramlist[0] == "*":
                return True
            else:
                if anagramlist[0] not in wordlist:
                    return False
                else:
                    wordlist.remove(anagramlist[0])
                    anagramlist.pop(0)
        return True

if tisa(word, anagram, wordlist, anagramlist):
    print("A")
else:
   print("N")