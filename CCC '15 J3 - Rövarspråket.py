word = input()
new = ""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for j in range(len(word)):
    if word[j] not in 'aeiou':
        con = 1

        new += word[j]

        place = alphabet.index(word[j])

        a = abs(place-0)
        min = a
        vowel = 'a'
        e = abs(place-4)
        if e < a:
            min = e
            vowel = 'e'
        i = abs(place-8)
        if i < min:
            min = i
            vowel = 'i'
        o = abs(place-14)
        if o < min:
            min = o
            vowel = 'o'
        u = abs(place-20)
        if u < min:
            min = u
            vowel = 'u'
        new += vowel

        while True:
            if word[j] == 'z':
                new += 'z'
                break
            else:
                place = alphabet.index(word[j])
                if alphabet[place+con] not in 'aeiou':
                    new += alphabet[place+con]
                    break
                else:
                    con += 1
    else:
        new += word[j]

print(new)