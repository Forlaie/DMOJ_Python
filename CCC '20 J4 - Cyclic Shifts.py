og = input()
test = input()

def cycle(test):
    for i in range(len(test)):
        if test in og:
            return "yes"
        else:
            test += test[0]
            test = test[1::]
    return "no"

print(cycle(test))