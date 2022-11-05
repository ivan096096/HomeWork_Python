# Task2
lst = ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday',
       'Sunday']
day1 = 6
day2 = 7
scan = int(input('Введите день- '))
for i in range(len(lst) + 1):
  if day1 == scan or day2 == scan:
    print("yes")
  else:
    print("no")