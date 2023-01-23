import re


def convert(match):
    test = match.group().split("/")
    str = match.group()
    if len(test) == 3 and len(test[0]) == 2 and len(test[1]) == 2 and len(test[2]) == 2:
        try:
            if 1 <= int(test[0]) <= 31:
                if 1 <= int(test[1]) <= 12:
                    year = int(test[2])
                    if year >= 25:
                        test[2] = "19" + test[2]
                    else:
                        test[2] = "20" + test[2]
                    str = test[0] + "/" + test[1] + "/" + test[2]
        except Exception:
            pass
    return str


def convert2(match):
    test = match.group().split(".")
    str = match.group()
    if len(test) == 3 and len(test[0]) == 2 and len(test[1]) == 2 and len(test[2]) == 2:
        try:
            if 1 <= int(test[2]) <= 31:
                if 1 <= int(test[1]) <= 12:
                    year = int(test[0])
                    if year >= 25:
                        test[0] = "19" + test[0]
                    else:
                        test[0] = "20" + test[0]
                    str = test[0] + "." + test[1] + "." + test[2]
        except Exception:
            pass
    return str

def convert3(match):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    test = re.split(r"\s|,\s", match.group())
    str = match.group()
    if len(test) == 3 and test[0] in months and len(test[1]) == 2 and len(test[2]) == 2:
        try:
            if 1 <= int(test[1]) <= 31:
                year = int(test[2])
                if year >= 25:
                    test[2] = "19" + test[2]
                else:
                    test[2] = "20" + test[2]
                str = test[0] + " " + test[1] + ", " + test[2]
        except Exception:
            pass
    return str

num = int(input())
for i in range(num):
    str = input()
    str = re.sub(r"\w+/\w+/\w+", convert, str)
    str = re.sub(r"\w+[.]\w+[.]\w+", convert2, str)
    str = re.sub(r"\w+\s\w+,\s\w+", convert3, str)
    print(str)