# class Node:
#     def __init__(self, letter):
#         self.letter = letter
#         self.right = None
#         self.left = None
#
#     def insert(self, data):
#         if data
#
# root = Node("")
# root.left = Node("")
# root.right = Node("")


num = int(input())
letters = []
codes = []
for i in range(num):
    info = input()
    letter, code = info.split()
    letters.append(letter)
    codes.append(code)

message = input()
result = ""
while message != "":
    for i in range(num):
        if message[:len(codes[i])] == codes[i]:
            result += letters[i]
            message = message[len(codes[i]):]
print(result)

