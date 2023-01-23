num = int(input())
sentence = "A long time ago in a galaxy "
for i in range(num):
    if i == num-1:
        sentence += "far "
    else:
        sentence += "far, "
sentence += "away..."
print(sentence)