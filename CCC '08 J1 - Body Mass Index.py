weight = input()
height = input()
bmi = weight/(height*height)
if bmi > 25:
  print "Overweight"
elif 18.5 < bmi < 25:
  print "Normal weight"
elif bmi < 18.5:
  print "Underweight"