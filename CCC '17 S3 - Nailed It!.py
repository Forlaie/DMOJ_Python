piecesOfWood = int(input())
woodLengths = input()
woodLengths = woodLengths.split()
woodLengths = list(map(int, woodLengths))
woodLengths.sort(reverse=True)
occurrencesOfWoodLengths = [0]*(woodLengths[0]+1)
occurrencesOfBoardLengths = [0]*(woodLengths[0]+woodLengths[1]+1)

for length in woodLengths:
    occurrencesOfWoodLengths[length] += 1

for totalLength in range(2, len(occurrencesOfBoardLengths)):
    for board1Length in range(1, totalLength//2+1):
        board2Length = totalLength-board1Length

        if board1Length > len(occurrencesOfWoodLengths)-1 or board2Length > len(occurrencesOfWoodLengths)-1:
            continue
        else:
            if board1Length == board2Length:
                if occurrencesOfWoodLengths[board1Length] > 1:
                    occurrencesOfBoardLengths[totalLength] += occurrencesOfWoodLengths[board1Length]//2
            else:
                occurrencesOfBoardLengths[totalLength] += min(occurrencesOfWoodLengths[board1Length], occurrencesOfWoodLengths[board2Length])
maxOccurrences = max(occurrencesOfBoardLengths)
print(maxOccurrences, occurrencesOfBoardLengths.count(maxOccurrences))



# from math import floor
# piecesOfWood = int(input())
# lengths = input()
# lengthsSep = lengths.split()
# woodLengths = list(map(int, lengthsSep))
# # The number of occurrences for every number
# occurrences = [0 for i in range(2001)]
# for i in woodLengths:
#     occurrences[i] += 1
# # number of boards for every length
# woods = [0 for i in range(4001)]
# for p in range(1, 4001):
#     for i in range(1, p//2+1):
#         j = p-i
#         if i > 2000 or j > 2000:
#             continue
#         if j == i:
#             woods[p] += occurrences[i]//2
#         elif occurrences[i] > 0 and occurrences[j] > 0:
#             woods[p] += min(occurrences[i], occurrences[j])
# a = max(woods)
# total = 0
# for i in woods:
#     if i == a:
#         total += 1
# print(a, total)

