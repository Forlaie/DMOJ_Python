words = ["one", "two", "three", "four", "five"]
words.sort(key=lambda x: (len(x), x))
print(words)