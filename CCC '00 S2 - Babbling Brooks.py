initialNumberOfStreams = int(input())
streamFlows = []
for i in range(initialNumberOfStreams):
    initialStreamFlow = int(input())
    streamFlows.append(initialStreamFlow)

action = int(input())
while action != 77:
    if action == 99:
        streamSplitPoint = int(input())
        streamSplitPoint -= 1
        originalStreamFlow = streamFlows[streamSplitPoint]
        streamFlowPercentageToLeft = int(input())
        streamFlows[streamSplitPoint] = originalStreamFlow * (streamFlowPercentageToLeft/100)
        streamFlows.insert(streamSplitPoint+1, originalStreamFlow * (1-(streamFlowPercentageToLeft/100)))
    else:
        streamJoinPoint = int(input())
        streamJoinPoint -= 1
        streamFlows[streamJoinPoint] += streamFlows[streamJoinPoint+1]
        streamFlows.pop(streamJoinPoint+1)
    action = int(input())

for i in range(len(streamFlows)-1):
    print(f"{int(streamFlows[i])}", end = " ")
print(f"{int(streamFlows[-1])}")