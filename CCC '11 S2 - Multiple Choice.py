choicelist = []
student = []
answer = []
questions = int(input())
number = 0
for i in range (questions*2):
    choice = input()
    choicelist.append(choice)
for i in range (questions):
    student.append(choicelist[i])
for i in range (questions):
    answer.append(choicelist[i+questions])
for i in range(questions):
    if student[i] == answer[i]:
        number += 1
print(number)