distance = int(input())
clubs = int(input())

clubHits = []
for i in range(clubs):
    hit = int(input())
    clubHits.append(hit)

dp = [float('inf') for i in range(distance+1)]
dp[0] = 0

for i in range(1, distance+1):
    for j in clubHits:
        if i - j >= 0:
            if 1 + dp[i-j] < dp[i]:
                dp[i] = 1 + dp[i-j]

if dp[-1] != float('inf'):
    print(f"Roberta wins in {dp[-1]} strokes.")
else:
    print("Roberta acknowledges defeat.")