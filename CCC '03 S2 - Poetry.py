verses = int(input())

for i in range(verses):
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()

    word1 = line1.split()[-1]
    word2 = line2.split()[-1]
    word3 = line3.split()[-1]
    word4 = line4.split()[-1]

    word1 = word1.lower()
    word2 = word2.lower()
    word3 = word3.lower()
    word4 = word4.lower()

    index1 = max(word1.rfind("a"), word1.rfind("e"), word1.rfind("i"), word1.rfind("o"), word1.rfind("u"))
    index2 = max(word2.rfind("a"), word2.rfind("e"), word2.rfind("i"), word2.rfind("o"), word2.rfind("u"))
    index3 = max(word3.rfind("a"), word3.rfind("e"), word3.rfind("i"), word3.rfind("o"), word3.rfind("u"))
    index4 = max(word4.rfind("a"), word4.rfind("e"), word4.rfind("i"), word4.rfind("o"), word4.rfind("u"))

    if index1 != -1:
        rhyme1 = word1[index1:]
    else:
        rhyme1 = word1

    if index2 != -1:
        rhyme2 = word2[index2:]
    else:
        rhyme2 = word2

    if index3 != -1:
        rhyme3 = word3[index3:]
    else:
        rhyme3 = word3

    if index4 != -1:
        rhyme4 = word4[index4:]
    else:
        rhyme4 = word4

    if rhyme1 == rhyme2 and rhyme2 == rhyme3 and rhyme3 == rhyme4:
        print("perfect")
    elif rhyme1 == rhyme2 and rhyme3 == rhyme4:
        print("even")
    elif rhyme1 == rhyme3 and rhyme2 == rhyme4:
        print("cross")
    elif rhyme1 == rhyme4 and rhyme2 == rhyme3:
        print("shell")
    else:
        print("free")