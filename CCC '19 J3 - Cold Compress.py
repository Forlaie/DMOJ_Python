lines = int(input())
count = 1
times = []
unique = []
result = ""

for i in range(lines):
    sentence = input()
    sentence = sentence + " "
    for j in range(len(sentence)-1):
        if sentence[j] == sentence[j+1]:
            count += 1
        else:
            times.append(count)
            unique.append(sentence[j])
            count = 1
    for m in range(len(times)):
        result += str(times[m]) + " " + str(unique[m]) + " "
    print(result.strip())
    result = ""
    times = []
    unique = []