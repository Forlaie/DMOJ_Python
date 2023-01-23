password = input()
uppercase = 0
lowercase = 0
digit = 0

if 8 <= len(password) <= 12:
    for i in range(len(password)):
        if password[i].isupper():
            uppercase += 1
        elif password[i].islower():
            lowercase += 1
        elif password[i].isdigit():
            digit += 1

if uppercase >= 2 and lowercase >= 3 and digit >= 1:
    print("Valid")
else:
    print("Invalid")