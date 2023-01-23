text=input()
happy = ":-)"
counth = text.count(happy)
sad = ":-("
counts = text.count(sad)
if counth==counts and counth>0 and counts>0:
  print "unsure"
elif counth==0 and counts==0:
  print "none"
elif counth>counts:
  print "happy"
else:
  print "sad"