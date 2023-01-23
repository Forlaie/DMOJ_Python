import re

def bfs(start, target):
    queue = [webpages.index(start)]
    visited = [False for i in range(numOfWebpages)]

    while len(queue) != 0:
        web = queue[0]
        queue.pop(0)

        for website in adjList[web]:
            if website == target:
                return "Can surf from " + start + " to " + target + "."
            website = webpages.index(website)
            if not visited[website]:
                queue.append(website)
                visited[website] = True
    return "Can't surf from " + start + " to " + target + "."

numOfWebpages = int(input())
webpages = []
adjList = [[] for i in range(numOfWebpages)]
str = ""
newWebpage = True
index = -1
count = 0

matches = re.findall(r"<A HREF=[\w:/.\"]+", str)
for match in matches:
    print(match)

while count != numOfWebpages:
    str = input()
    if newWebpage:
        webpages.append(str)
        newWebpage = False
        index += 1

    if re.search(r"</HTML>", str):
        newWebpage = True
        count += 1

    matches = re.findall(r"<A HREF=[\w:/.\"]+", str)
    for match in matches:
        url = match.split("\"")
        adjList[index].append(url[1])
        print("Link from " + webpages[index] + " to " + url[1])

while True:
    first = input()
    if first == "The End":
        break
    second = input()
    print(bfs(first, second))

# import re
#
# str = input() # <A HREF="http://abc.def/ghi">
# match = re.search("\"[\w:/.]+", str)
# print(match.group()) # "http://abc.def/ghi