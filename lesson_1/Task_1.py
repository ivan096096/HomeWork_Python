# Task1
var = [0, 1]
for x in var:
  for y in var:
    for z in var:
      st1 = not (x or y or z)
      st2 = not (x) and not (y) and not (z)
      resalt = st1 == st2
      print(resalt)
