info = input()
city, temp = info.split()
temp = int(temp)

dict = {temp: city}

while city != "Waterloo":
    info = input()
    city, temp = info.split()
    temp = int(temp)
    dict[temp] = city

listt = dict.keys()
listt = list(listt)
listt.sort()
min = listt[0]

print(dict[min])

