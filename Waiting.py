griffy = input()
school = input()
gh, gm, gs = griffy.split(":")
sh, sm, ss = school.split(":")
gh = int(gh)
gm = int(gm)
gs = int(gs)
sh = int(sh)
sm = int(sm)
ss = int(ss)
time = (sh-gh)*60*60 + (sm-gm)*60 + (ss-gs)
print(time)