# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# # n = int(input('Введите число - '))
def multiplier(n):
 d = 2
 list1 = []
 while d * d <= n:
  if n % d == 0:
    list1.append(d)
    n //= d
  else:
    d += 1
 if n > 1:
  list1.append(n)
 return list1


print(multiplier(int(input('Введите число - '))))
