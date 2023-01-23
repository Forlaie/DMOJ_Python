def solve(cookies, people):
    if cookies <= people:
        return 1
    if people == 1:
        return 1
    out = 0
    for i in range(cookies/people):
        out += solve(cookies-i*people, people-1)
    return out

#for (int add = 0; add*(people+1) <= cookies)

def main():
    cookies = int(input())
    people = int(input())
    print(solve(cookies-people, people))
main()