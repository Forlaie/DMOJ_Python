friends = int(input())
position = []
speed = []
hearing = []

def timeTaken(location):
    time = 0
    for i in range(friends):
        left = position[i] - hearing[i]
        right = position[i] + hearing[i]
        if left <= location <= right:
            continue
        closest = min(abs(location-left), abs(location-right))
        time += closest*speed[i]
    return time

r = 0
l = float('inf')
for i in range(friends):
    p, w, d = list(map(int, input().split()))
    position.append(p)
    speed.append(w)
    hearing.append(d)
    if p > r:
        r = p
    if p < l:
        l = p

# ternary search
best = float('inf')
for i in range(60):
    delta = (r-l)//3
    m1 = l + delta
    m2 = r - delta
    t1 = timeTaken(m1)
    t2 = timeTaken(m2)
    best = min(best, t1, t2)

    if t1 > t2:
        l = m1
    if t2 > t1:
        r = m2
print(best)