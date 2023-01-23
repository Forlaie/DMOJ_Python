# Brute Force
# word = input()
# num = 0
#
# for i in range(len(word)):
#     for j in range(i+1, len(word)+1):
#         paliTest = word[i:j]
#         reversePali = paliTest[::-1]
#         if paliTest == reversePali:
#             if len(paliTest) > num:
#                 num = len(paliTest)
# print(num)


# Trying to do the O(n^2) version myself (idk if its right)
# word = input()
# num = 0
# adjustedWord = "#"
#
# def longestPalindromeFromCenter(word, left, right, num):
#     if left <= 0 or right >= len(word):
#         return num
#     else:
#         if word[left] == word[right]:
#             num += 2
#             left -= 2
#             right += 2
#             return longestPalindromeFromCenter(word, left, right, num)
#         else:
#             return num
#
# for i in range(len(word)):
#     adjustedWord += word[i]
#     adjustedWord += "#"
#
# for i in range(len(adjustedWord)):
#     if adjustedWord[i] == "#":
#         length = longestPalindromeFromCenter(adjustedWord, i-1, i+1, 0)
#     else:
#         length = longestPalindromeFromCenter(adjustedWord, i-2, i+2, 1)
#     if length > num:
#         num = length
# print(num)

# Manacher’s Algorithm
# word = input()
# adjustedWord = "$#"
# for i in range(len(word)):
#     adjustedWord += word[i]
#     adjustedWord += "#"
# adjustedWord += "@"
#
# c = 1 #center
# r = 1 #right boundary
# p = [0 for i in range(len(adjustedWord))] #longest palindrome from center length (how far away its going from the center)
#
# for i in range(1, len(adjustedWord)-1):
#     mirror = 2 * c - i
#     if i < r:
#         if i+p[mirror] > r:
#             p[i] = r - i
#         else:
#             p[i] = p[mirror]
#
#     while adjustedWord[i + (p[i] + 1)] == adjustedWord[i - (p[i] + 1)]:
#         p[i] += 1
#
#     if r < p[i] + i:
#         r = p[i] + i
#
#     if p[c] < p[i]:
#         c = i
#
# p.sort(reverse=True)
# print(p[0])

# "Official" Manacher's Algorithm
word = input()
T = "$#"
for i in range(len(word)):
    T += word[i]
    T += "#"
T += "@"

P = [0 for i in range(len(T))]
C = 0
R = 0

for i in range(len(T)-1):
    mirr = 2*C - i

    if i < R:
        P[i] = min(R-i, P[mirr])

    while T[i + (1+P[i])] == T[i-(1+P[i])]:
        P[i] += 1

        if i + P[i] > R:
            C = i # i think my mistake was that choosing a new center doesnt mean that its the longest, just that it has the potential
            R = i + P[i]

P.sort(reverse=True)
print(P[0])